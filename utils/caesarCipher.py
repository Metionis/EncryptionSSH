def caesar_encrypt(text, shift):
    """Encrypt text using Caesar cipher."""
    encrypted_text = ''
    for char in text:
        if char.isalpha():  # Encrypt only alphabetic characters
            shift_amount = shift % 26
            base = 'A' if char.isupper() else 'a'
            encrypted_char = chr((ord(char) - ord(base) + shift_amount) % 26 + ord(base))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters are not encrypted
    return encrypted_text.encode('utf-8')  # Return as bytes

def caesar_decrypt(encrypted_text, shift):
    """Decrypt text using Caesar cipher."""
    decrypted_text = caesar_encrypt(encrypted_text, -shift)  # Encrypt with negative shift to decrypt
    return decrypted_text  # Return as bytes

