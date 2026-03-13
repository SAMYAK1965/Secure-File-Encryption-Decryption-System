# 🔐 Secure File Encryption & Decryption System

A web-based tool that allows users to securely **encrypt folders and download them as encrypted ZIP files**.
The system uses a **Flask backend API** and a **Vue.js frontend interface** to process files securely.

---

# 🚀 Features

* Upload an entire folder
* Encrypt multiple files at once
* Download encrypted files as a ZIP archive
* Drag-and-drop folder support
* Multithreaded encryption for faster processing
* File history stored using a database

---

# 🛠 Tech Stack

### Backend

* Python
* Flask
* Flask-CORS
* Flask-SQLAlchemy
* Cryptography

### Frontend

* Vue.js
* Axios
* Bootstrap

### Deployment

* Render (Backend Hosting)
* Vercel (Frontend Hosting)
* GitHub (Version Control)

---

# 📂 Project Structure

```
Secure-File-Encryption-Decryption-System
│
├── backend
│   ├── app.py
│   ├── crypto_utils.py
│   ├── config.py
│   ├── models.py
│   ├── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── components
│   │   │   └── EncryptTool.vue
│   │   └── App.vue
│
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/SAMYAK1965/Secure-File-Encryption-Decryption-System.git
cd Secure-File-Encryption-Decryption-System
```

---

## 2️⃣ Setup Backend

Navigate to backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run Backend Server

```bash
python app.py
```

Backend will start at:

```
http://localhost:5000
```

---

## 4️⃣ Run Frontend

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run development server:

```bash
npm run dev
```

Frontend will start at:

```
http://localhost:5173
```

---

# 🌐 Live Deployment

Frontend (Vercel):

```
https://secure-file-encryption-decryption-s.vercel.app
```

Backend API (Render):

```
https://secure-file-encryption-decryption-system.onrender.com
```

---

# 🔄 Workflow

```
User uploads folder
↓
Frontend (Vue.js)
↓
Backend API (Flask)
↓
Files encrypted
↓
ZIP file generated
↓
Encrypted folder downloaded
```

---

# 🔒 Security

Files are encrypted using **AES-based encryption through the Python Cryptography library**, ensuring strong file protection.

---

# 👨‍💻 Author

Samyak Gajbhiye
Electronics & Telecommunication Engineering
G.H. Raisoni College of Engineering, Nagpur

---

# 📜 License

This project is open-source and available under the **MIT License**.
