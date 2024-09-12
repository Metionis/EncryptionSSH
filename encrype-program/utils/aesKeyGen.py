from Crypto.Random import get_random_bytes
import os

def generate_aes_key(key_size=16):
    """Generate a new AES key and save it to a file."""
    key = get_random_bytes(key_size)
    with open('aes_key.bin', 'wb') as f:
        f.write(key)
    print("AES key generated and saved.")

def load_aes_key(file_path='aes_key.bin'):
    """Load the AES key from a file."""
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading AES key from {file_path}: {e}")
        return None

