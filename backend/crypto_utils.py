import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

KEY = b'0123456789abcdef0123456789abcdef'


def encrypt_file(input_path, output_path):

    iv = os.urandom(16)

    cipher = Cipher(
        algorithms.AES(KEY),
        modes.CBC(iv),
        backend=default_backend()
    )

    encryptor = cipher.encryptor()

    with open(input_path, "rb") as f:
        data = f.read()

    padder = padding.PKCS7(128).padder()
    padded = padder.update(data) + padder.finalize()

    encrypted = encryptor.update(padded) + encryptor.finalize()

    with open(output_path, "wb") as f:
        f.write(iv + encrypted)


def decrypt_file(input_path, output_path):

    with open(input_path, "rb") as f:
        data = f.read()

    iv = data[:16]
    encrypted = data[16:]

    cipher = Cipher(
        algorithms.AES(KEY),
        modes.CBC(iv),
        backend=default_backend()
    )

    decryptor = cipher.decryptor()

    decrypted = decryptor.update(encrypted) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    original = unpadder.update(decrypted) + unpadder.finalize()

    with open(output_path, "wb") as f:
        f.write(original)