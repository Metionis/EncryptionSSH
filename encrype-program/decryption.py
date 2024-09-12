import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from utils.aesKeyGen import load_aes_key  # Ensure this function loads the correct AES key
from utils.keysInteract import *
from Crypto.Util.Padding import unpad


def main_decrypt():
    project_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the decryption script
    encrypted_keys_dir = project_dir
    decrypted_keys_dir = os.path.expanduser('~/.ssh')

    if not os.path.exists(encrypted_keys_dir):
        print(f"The directory {encrypted_keys_dir} does not exist.")
        return
    
    if not os.path.exists(decrypted_keys_dir):
        os.makedirs(decrypted_keys_dir)

    # NOTE: Replace the following line with the actual AES key used during encryption
    aes_key = load_aes_key()  # Example placeholder; you need the actual key here

    try:
        files = os.listdir(encrypted_keys_dir)
        for file in files:
            file_path = os.path.join(encrypted_keys_dir, file)
            if os.path.isfile(file_path):
                print('Wait for 3 seconds to begin decryption...')
                time.sleep(3)
                
                encrypted_key_content = read_encrypted_key(file_path)
                if encrypted_key_content:
                    print(f"Read encrypted key from {file_path}")

                    decrypted_key = decrypt_key(encrypted_key_content, aes_key)
                    if decrypted_key:
                        original_file_name = file.rsplit('.txt', 1)[0]
                        decrypted_key_path = os.path.join(decrypted_keys_dir, original_file_name)
                        save_key(decrypted_key_path, decrypted_key)
                        print(f"Decrypted key saved to {decrypted_key_path}")

                        # Delete the encrypted file after successful decryption
                        # delete_key(file_path)
                    else:
                        print(f"Failed to decrypt key in {file_path}")
                else:
                    print(f"Failed to read encrypted key from {file_path}")

        print('Decryption process completed.')
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

if __name__ == "__main__":
    main_decrypt()