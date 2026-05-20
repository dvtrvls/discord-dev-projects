# 🔐 RinLock 2.0

A simple command-line password manager built with Python, SQLite, and Fernet encryption.

---

# ⚙️ Features

- AES-style encryption using `Fernet`
- Store app credentials (app, username, password)
- Master password protection
- Change master password
- Delete saved accounts
- Duplicate prevention system
- Cross-platform storage support (Windows + Linux)
- Interactive TUI mode with keyboard navigation (new)

---

# 🚀 Installation

## 1. Install dependency

```bash
pip install -r requirements.txt
```

## 2. Run the program

```bash
python3 r2.py
```

---

# 📌 Commands

## 🔹 Add account

```bash
python3 r2.py add <app> <username> <password>
```

Example:

```bash
python3 r2.py add facebook john123 mypass123
```

---

## 🔹 Set master password (first time only)

```bash
python3 r2.py setpass <password>
```

Example:

```bash
python3 r2.py setpass rin123
```

---

## 🔹 Change master password

```bash
python3 r2.py changepass <old_password> <new_password>
```

Example:

```bash
python3 r2.py changepass rin123 newpass456
```

---

## 🔹 View saved passwords

```bash
python3 r2.py view <master_password>
```

Example:

```bash
python3 r2.py view rin123
```

---

## 🔹 Delete account

```bash
python3 r2.py delete <app>
```

Example:

```bash
python3 r2.py delete facebook
```

---

## 🔹 Interactive TUI mode (new)

```Launches a full interactive terminal interface. Navigate accounts with keyboard commands, reveal or hide passwords on demand, and delete entries — all without exposing anything in plain text.```


## Key Actions

| Key / Action | Description                     |
|--------------|---------------------------------|
| **j** or **↓** | Move down                      |
| **k** or **↑** | Move up                        |
| **v**          | Reveal / hide selected password |
| **d**          | Delete selected account         |
| **q**          | Quit and lock vault             |


---

# 🔐 Security Notes

- Passwords are encrypted using Fernet
- Encryption key is stored in `secret.key`
- Master password is stored in SQLite database
- DO NOT delete `secret.key` or data cannot be recovered
- Passwords typed in TUI mode are hidden from terminal display

---

# 📁 Storage (NEW UPDATE)

Database and encryption files are now stored in hidden system directories depending on the operating system.

## 🪟 Windows

```text
C:\Users\<User>\AppData\Roaming\RinLock
```

Files:

```text
rinlock.db   → database storage
secret.key   → encryption key
```

---

## 🐧 Linux

```text
~/.local/share/RinLock
```

Files:

```text
rinlock.db   → database storage
secret.key   → encryption key
```

---

# ⚠️ Warning

This project is for educational purposes only.

Do not use it as a production password manager.

---

# 🧠 Example Workflow

```bash
python3 r2.py setpass rin123

python3 r2.py add facebook aldrix mypass123
python3 r2.py add github aldrix ghtoken456

python3 r2.py ui
```
---

👥 Contributors

@iamjhonaldrix — core CLI engine
@dvtrv1s — TUI mode, Linux path support fix