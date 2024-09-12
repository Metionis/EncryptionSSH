from Crypto.Cipher import AES
import os

IV_FILE_PATH = os.path.expanduser(r'D:\NCKH\Projects\Cyber Sercurity Projects\SSH_Ceasar_Encryption\sshKeys\iv.txt')

def generate_iv():
    """Generates a fixed IV and saves it to a .txt file."""
    fixed_iv = b'\x00' * AES.block_size  # Example: 16 bytes of zeroes

    try:
        with open(IV_FILE_PATH, 'wb') as f:
            f.write(fixed_iv)
        print(f"Fixed IV saved to {IV_FILE_PATH}")
    except Exception as e:
        print(f"Error saving IV to {IV_FILE_PATH}: {e}")

def load_iv(file_path=IV_FILE_PATH):
    """Loads the IV from the .txt file."""
    try:
        with open(file_path, 'rb') as f:
            iv = f.read()
            if len(iv) != AES.block_size:
                raise ValueError("IV length is not valid.")
            return iv
    except Exception as e:
        print(f"Error loading IV from {file_path}: {e}")
        return None
