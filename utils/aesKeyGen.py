from Crypto.Random import get_random_bytes
import os

AES_KEY_FILE_PATH = os.path.expanduser(r'D:\NCKH\Projects\Cyber Sercurity Projects\SSH_Ceasar_Encryption\sshKeys\aess_key.txt')

def generate_aes_key(key_size=16):
    """Generate a new AES key and save it to a file."""
    key = get_random_bytes(key_size)
    with open(AES_KEY_FILE_PATH, 'wb') as f:
        f.write(key)
    print(f"AES key generated and saved to {AES_KEY_FILE_PATH}")

def load_aes_key(file_path=AES_KEY_FILE_PATH):
    """Load the AES key from a file."""
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading AES key from {file_path}: {e}")
        return None
