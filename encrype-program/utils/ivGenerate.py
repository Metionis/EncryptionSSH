import os
from Crypto.Random import get_random_bytes

# Define a fixed path for the IV file
IV_FILE_PATH = os.path.expanduser('~/iv.bin')

def generate_iv():
    """
    Generates a fixed IV and saves it to a file.
    """
    # Define a fixed IV (must be 16 bytes for AES)
    fixed_iv = b'\x00' * AES.block_size  # Example: 16 bytes of zeroes

    try:
        with open(IV_FILE_PATH, 'wb') as f:
            f.write(fixed_iv)
        print(f"Fixed IV saved to {IV_FILE_PATH}")
    except Exception as e:
        print(f"Error saving IV to {IV_FILE_PATH}: {e}")

def load_iv():
    """
    Loads the IV from the file.
    """
    try:
        with open(IV_FILE_PATH, 'rb') as f:
            iv = f.read()
            if len(iv) != AES.block_size:
                raise ValueError("IV length is not valid.")
            return iv
    except Exception as e:
        print(f"Error loading IV from {IV_FILE_PATH}: {e}")
        return None
