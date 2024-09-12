import os
from utils.caesarCipher import caesar_decrypt
from utils.keysInteract import read_key, save_decrypted_key

def decrypt_key(file_path, shift):
    """Decrypt the content of the file using Caesar cipher."""
    try:
        # Read encrypted key
        encrypted_key = read_key(file_path)
        if encrypted_key is None:
            raise ValueError(f"Could not read encrypted key from {file_path}")

        # Decrypt key
        decrypted_key = caesar_decrypt(encrypted_key, shift)
        print(f"Decrypted key from {file_path}.")

        return decrypted_key

    except Exception as e:
        print(f"An error occurred while decrypting the key: {e}")
        return None

def restore_keys(encrypted_key_dir, decrypted_key_dir, shift_amount):
    """Restore decrypted keys to their original location."""
    try:
        if os.path.exists(encrypted_key_dir):
            print(f"Found encrypted keys directory, restoring keys...")

            for file_name in os.listdir(encrypted_key_dir):
                if file_name.endswith('.txt'):  # Only process .txt files
                    file_path = os.path.join(encrypted_key_dir, file_name)
                    original_file_path = os.path.join(decrypted_key_dir, file_name.replace('.txt', ''))

                    # Decrypt the key and save to a temporary file
                    decrypted_key = decrypt_key(file_path, shift_amount)
                    if decrypted_key:
                        # Restore decrypted key to the original location
                        with open(original_file_path, 'wb') as f:
                            f.write(decrypted_key)
                        print(f"Restored key to {original_file_path}.")
                    else:
                        print(f"Failed to restore key for {file_name}.")

        else:
            print("Encrypted keys directory does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    encrypted_key_dir = os.path.expanduser('D:/Github Projects/EncryptionSSH')  # Directory with encrypted .txt files
    decrypted_key_dir = os.path.expanduser('C:/Users/Admin/.ssh/')  # Directory where decrypted files are stored
    shift_amount = 3  # Example shift amount for Caesar cipher

    try:
        restore_keys(encrypted_key_dir, decrypted_key_dir, shift_amount)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
