import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define Caesar cipher shift amount from .env with default value
SHIFT_AMOUNT = os.getenv('KEY_SHIFT')
if SHIFT_AMOUNT is None:
    print("KEY_SHIFT not found in .env, using default value 3.")
    # SHIFT_AMOUNT = 3
else:
    SHIFT_AMOUNT = int(SHIFT_AMOUNT)
    print(SHIFT_AMOUNT)
    print(type(SHIFT_AMOUNT))

# Continue with the rest of your code...
SSH_KEY_DIR = os.getenv('SSH_KEY_DIR')
if SSH_KEY_DIR is None:
  print('Not found SSH_KEY_DIR')
else:
  SSH_KEY_DIR = str(SSH_KEY_DIR)
  print(SSH_KEY_DIR)
  print(type(SSH_KEY_DIR))
  
ENCRYPTED_KEY_DIR = os.getenv('ENCRYPTED_KEY_DIR')
if SSH_KEY_DIR is None:
  print('Not found ENCRYPTED_KEY_DIR')
else:
  ENCRYPTED_KEY_DIR = str(ENCRYPTED_KEY_DIR)
  print(ENCRYPTED_KEY_DIR)
  print(type(ENCRYPTED_KEY_DIR))
  
DECRYPTED_KEY_DIR = os.getenv('DECRYPTED_KEY_DIR')
if DECRYPTED_KEY_DIR is None:
  print('Not found DECRYPTED_KEY_DIR')
else:
  DECRYPTED_KEY_DIR = str(DECRYPTED_KEY_DIR)
  print(DECRYPTED_KEY_DIR)
  print(type(DECRYPTED_KEY_DIR))