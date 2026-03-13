from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import io
import zipfile
import shutil
from concurrent.futures import ThreadPoolExecutor

from config import UPLOAD_FOLDER, ENCRYPTED_FOLDER, DATABASE_URI
from crypto_utils import encrypt_file
from models import db, FileRecord

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)


# -------------------------
# PROCESS FILE
# -------------------------

def process_file(file):

    filename = file.filename

    upload_path = os.path.join(UPLOAD_FOLDER, filename)
    encrypted_path = os.path.join(ENCRYPTED_FOLDER, filename + ".enc")

    os.makedirs(os.path.dirname(upload_path), exist_ok=True)
    os.makedirs(os.path.dirname(encrypted_path), exist_ok=True)

    file.save(upload_path)

    encrypt_file(upload_path, encrypted_path)

    record = FileRecord(
        original_name=filename,
        encrypted_name=filename + ".enc",
        status="encrypted"
    )

    db.session.add(record)
    db.session.commit()


# -------------------------
# ENCRYPT FOLDER
# -------------------------

@app.route("/encrypt-folder", methods=["POST"])
def encrypt_folder():

    files = request.files.getlist("files")

    if os.path.exists(ENCRYPTED_FOLDER):
        shutil.rmtree(ENCRYPTED_FOLDER)

    os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)

    with ThreadPoolExecutor(max_workers=6) as executor:
        executor.map(process_file, files)

    memory_file = io.BytesIO()

    with zipfile.ZipFile(memory_file, "w", zipfile.ZIP_DEFLATED) as zf:

        for root, dirs, files in os.walk(ENCRYPTED_FOLDER):

            for file in files:

                file_path = os.path.join(root, file)

                arcname = os.path.relpath(file_path, ENCRYPTED_FOLDER)

                zf.write(file_path, arcname)

    memory_file.seek(0)

    return send_file(
        memory_file,
        download_name="encrypted_folder.zip",
        as_attachment=True
    )


# -------------------------
# VIEW FILE HISTORY
# -------------------------

@app.route("/files")
def files():

    data = FileRecord.query.all()

    result = []

    for f in data:

        result.append({
            "id": f.id,
            "original": f.original_name,
            "encrypted": f.encrypted_name,
            "status": f.status
        })

    return jsonify(result)


# -------------------------
# RUN SERVER (FOR RENDER)
# -------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)