import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ENCRYPTED_FOLDER = os.path.join(BASE_DIR, "encrypted")
DECRYPTED_FOLDER = os.path.join(BASE_DIR, "decrypted")

DATABASE_URI = "sqlite:///database.db"