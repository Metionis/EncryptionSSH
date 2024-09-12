import os
import time
import re

def is_private_key(file_path):
    """
    Kiểm tra xem file có phải là SSH private key hay không bằng cách kiểm tra nội dung.
    """
    try:
        with open(file_path, 'r') as f:
            first_line = f.readline()
            return bool(re.match(r'-----BEGIN (OPENSSH) PRIVATE KEY-----', first_line))
    except Exception:
        return False

def is_public_key(file_path):
    """
    Kiểm tra xem file có phải là SSH public key hay không bằng cách kiểm tra nội dung.
    """
    try:
        with open(file_path, 'r') as f:
            first_word = f.readline().split()[0]
            return first_word in ['ssh-rsa', 'ssh-ed25519', 'ssh-dss', 'ecdsa-sha2-nistp256', 'ecdsa-sha2-nistp384', 'ecdsa-sha2-nistp521']
    except Exception:
        return False