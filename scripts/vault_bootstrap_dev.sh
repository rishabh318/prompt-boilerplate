#!/usr/bin/env bash
set -euo pipefail

VAULT_ADDR="http://127.0.0.1:8200"
VAULT_TOKEN="root"

echo "===> Using Vault at $VAULT_ADDR with token $VAULT_TOKEN"

# Wrapper: run vault CLI inside container, support stdin
vault_exec() {
  if [ -t 0 ]; then
    docker exec \
      -e VAULT_ADDR=$VAULT_ADDR \
      -e VAULT_TOKEN=$VAULT_TOKEN \
      vault vault "$@"
  else
    docker exec -i \
      -e VAULT_ADDR=$VAULT_ADDR \
      -e VAULT_TOKEN=$VAULT_TOKEN \
      vault vault "$@"
  fi
}

echo "===> Enabling KV v2 at path 'kv/'"
vault_exec secrets enable -path=kv -version=2 kv || echo "KV already enabled"

echo "===> Enabling Transit"
vault_exec secrets enable transit || echo "Transit already enabled"

echo "===> Creating transit key 'app-shared'"
vault_exec write -f transit/keys/app-shared

echo "===> Writing sample secrets into KV v2"
vault_exec kv put kv/google/translate api_key="dummy-google-api-key"
vault_exec kv put kv/openai api_key="dummy-openai-key"
vault_exec kv put kv/databases/mongo uri="mongodb://user:pass@localhost:27017/db"
vault_exec kv put kv/databases/postgres uri="postgresql://user:pass@localhost:5432/db"
vault_exec kv put kv/minio access_key="minioadmin" secret_key="minioadmin123"

echo "===> Creating policy 'app-policy'"
cat <<'HCL' | vault_exec policy write app-policy -
path "transit/encrypt/app-shared" { capabilities = ["update"] }
path "transit/decrypt/app-shared" { capabilities = ["update"] }
path "transit/keys/app-shared/rotate" { capabilities = ["update"] }
path "transit/keys/app-shared" { capabilities = ["read","update"] }
path "kv/data/*" { capabilities = ["read"] }
HCL

echo "===> Enabling AppRole auth method"
vault_exec auth enable approle || echo "AppRole already enabled"

echo "===> Creating role 'app-role' bound to 'app-policy'"
vault_exec write auth/approle/role/app-role \
  token_policies="app-policy" \
  secret_id_ttl=60m \
  token_ttl=60m \
  token_max_ttl=120m

ROLE_ID=$(vault_exec read -field=role_id auth/approle/role/app-role/role-id)
SECRET_ID=$(vault_exec write -f -field=secret_id auth/approle/role/app-role/secret-id)

echo "===> AppRole created successfully"
echo "ROLE_ID: $ROLE_ID"
echo "SECRET_ID: $SECRET_ID"
