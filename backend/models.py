from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class FileRecord(db.Model):

    __tablename__ = "files"

    id = db.Column(db.Integer, primary_key=True)

    original_name = db.Column(db.String(200))

    encrypted_name = db.Column(db.String(200))

    status = db.Column(db.String(50))