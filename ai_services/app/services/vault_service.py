from app.clients.vault_client import VaultClient

vault_client = VaultClient()

def encrypt_text(plaintext: str) -> str:
    return vault_client.encrypt(plaintext)

def decrypt_text(ciphertext: str) -> str:
    return vault_client.decrypt(ciphertext)

def rotate_key() -> None:
    vault_client.rotate_key()

def fetch_db_creds(role: str) -> dict:
    return vault_client.get_db_creds(role)
