import os
import time
import re

from utils.checkKey import is_private_key, is_public_key

# from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

def find_ssh_keys(ssh_dir):
    """
    Tìm và phân loại các SSH keys trong thư mục .ssh.
    """
    ssh_keys = {
        'private_keys': [],
        'public_keys': []
    }

    try:
        files = os.listdir(ssh_dir)
        for file in files:
            file_path = os.path.join(ssh_dir, file)
            if os.path.isfile(file_path):
                if is_private_key(file_path):
                    ssh_keys['private_keys'].append(file)
                elif is_public_key(file_path):
                    ssh_keys['public_keys'].append(file)
    except Exception as e:
        print(f"An error occurred while listing files: {e}")

    return ssh_keys

def encrypt_key(key_content, aes_key, iv):
    """
    Encrypts a key using AES with the provided key and IV.
    """
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(key_content, AES.block_size))
    return iv + ciphertext

def read_key(file_path):
    """Read the content of a key file."""
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading key from {file_path}: {e}")
        return None

def delete_key(file_path):
    """
    Xóa key sau khi mã hóa.
    """
    try:
        os.remove(file_path)
        print(f"Deleted original key file: {file_path}")
    except Exception as e:
        print(f"Failed to delete key file {file_path}: {e}")

def save_encrypted_key(file_path, encrypted_key):
    """Save the encrypted key to a file."""
    try:
        with open(file_path, 'wb') as f:
            f.write(encrypted_key)
    except Exception as e:
        print(f"Error saving encrypted key to {file_path}: {e}")


def decrypt_key(encrypted_key, aes_key, iv):
    """Decrypt the encrypted key using AES."""
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    decrypted_key = unpad(cipher.decrypt(encrypted_key), AES.block_size)
    return decrypted_key

def read_key(file_path):
    """Read the contents of a key file."""
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading key from {file_path}: {e}")
        return None

def save_decrypted_key(file_path, decrypted_key):
    """Save the decrypted key to a file."""
    try:
        with open(file_path, 'wb') as f:
            f.write(decrypted_key)
        print(f"Decrypted key saved to {file_path}")
    except Exception as e:
        print(f"Error saving decrypted key to {file_path}: {e}")