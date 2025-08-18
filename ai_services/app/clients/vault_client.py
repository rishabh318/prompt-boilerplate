from hvac import Client
import os
from typing import Optional

class VaultClient:
    def __init__(self) -> None:
        self.client = Client(url=os.getenv("VAULT_ADDR"))
        token = os.getenv("VAULT_TOKEN")
        if not token:
            raise ValueError("Vault token not found in environment variables")
        self.client.token = token
        self.key_name = os.getenv("VAULT_KEY_NAME", "my-encryption-key")

    def encrypt(self, plaintext: str) -> str:
        response = self.client.secrets.transit.encrypt_data(
            name=self.key_name,
            plaintext=plaintext.encode("utf-8").hex()
        )
        return response["data"]["ciphertext"]

    def decrypt(self, ciphertext: str) -> str:
        response = self.client.secrets.transit.decrypt_data(
            name=self.key_name,
            ciphertext=ciphertext
        )
        return bytes.fromhex(response["data"]["plaintext"]).decode("utf-8")

    def rotate_key(self) -> None:
        self.client.secrets.transit.rotate_key(name=self.key_name)

    def get_db_creds(self, role: str) -> Optional[dict]:
        return self.client.secrets.database.generate_credentials(role=role)["data"]
