from cryptography.fernet import Fernet
import os
import json

# Generate a key for development. In production, load from env var securely.
_DEV_KEY = Fernet.generate_key()
SECRET_KEY = os.getenv("ENCRYPTION_KEY", _DEV_KEY.decode())
fernet = Fernet(SECRET_KEY.encode())

def encrypt_data(payload: dict) -> str:
    """Encrypts a Python dictionary payload into an encrypted string."""
    json_data = json.dumps(payload).encode('utf-8')
    return fernet.encrypt(json_data).decode('utf-8')

def decrypt_data(encrypted_str: str) -> dict:
    """Decrypts a string back into a Python dictionary."""
    decrypted_data = fernet.decrypt(encrypted_str.encode('utf-8'))
    return json.loads(decrypted_data.decode('utf-8'))
