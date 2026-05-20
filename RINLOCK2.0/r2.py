import sqlite3
import sys
import os
from cryptography.fernet import Fernet
import platform

if platform.system() == "Windows":
    BASE_DIR = os.getenv("APPDATA")
else:
    BASE_DIR = os.path.expanduser("~/.local/share")

APP_DIR = os.path.join(BASE_DIR, "RinLock")
os.makedirs(APP_DIR, exist_ok=True)

KEY_PATH = os.path.join(APP_DIR, "secret.key")
DB_PATH = os.path.join(APP_DIR, "rinlock.db")

try:
    with open(KEY_PATH, "rb") as key_file:
        key = key_file.read()

except FileNotFoundError:
    key = Fernet.generate_key()

    with open(KEY_PATH, "wb") as key_file:
        key_file.write(key)

cipher = Fernet(key)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    app TEXT,
    username TEXT,
    password TEXT
);

CREATE TABLE IF NOT EXISTS settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    master_password TEXT
);
""")

conn.commit()

if len(sys.argv) < 2:
    print("""
Usage:

python3 r2.py add <app> <username> <password>
python3 r2.py view <password>
python3 r2.py delete <app>
python3 r2.py setpass <password>
python3 r2.py changepass <old_password> <new_password>
""")
    
    sys.exit()

command = sys.argv[1].lower()


if command == "add":

    if len(sys.argv) != 5:
        print("Usage: python3 r2.py add <app> <username> <password>")
        sys.exit()

    app = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]

    encrypted_password = cipher.encrypt(password.encode()).decode()

    cursor.execute("""
        SELECT * FROM accounts
        WHERE app = ? AND username = ?
    """, (app, username))

    existing = cursor.fetchone()

    if existing:
        print("This account already exists!")
        sys.exit()

    cursor.execute(
        "INSERT INTO accounts (app, username, password) VALUES (?, ?, ?)",
        (app, username, encrypted_password)
    )

    conn.commit()

    print("Password saved!")

elif command == "setpass":

    if len(sys.argv) != 3:
        print("Usage: python3 r2.py setpass <password>")
        sys.exit()

    password = sys.argv[2]

    cursor.execute("SELECT * FROM settings")
    existing = cursor.fetchone()

    if existing:
        print("Master password already exists!")
        print("Use: python3 r2.py changepass <old> <new>")
        sys.exit()

    else:
        cursor.execute(
            "INSERT INTO settings (master_password) VALUES (?)",
            (password,)
        )

    conn.commit()

    print("Master password saved!")

elif command == "changepass":

    if len(sys.argv) != 4:
        print("Usage: python3 r2.py changepass <old_password> <new_password>")
        sys.exit()

    old_password = sys.argv[2]
    new_password = sys.argv[3]

    cursor.execute("SELECT master_password FROM settings")
    result = cursor.fetchone()

    if not result:
        print("No master password set.")
        sys.exit()

    saved_password = result[0]

    if old_password != saved_password:
        print("Wrong old password!")
        sys.exit()

    cursor.execute(
        "UPDATE settings SET master_password = ?",
        (new_password,)
    )

    conn.commit()

    print("Master password changed successfully!")

elif command == "view":

    if len(sys.argv) != 3:
        print("Usage: python3 r2.py view <master_password>")
        sys.exit()

    entered_password = sys.argv[2]

    cursor.execute("SELECT master_password FROM settings")
    result = cursor.fetchone()

    if not result:
        print("No master password set.")
        sys.exit()

    saved_password = result[0]

    if entered_password != saved_password:
        print("Wrong master password!")
        sys.exit()

    cursor.execute("SELECT app, username, password FROM accounts")

    rows = cursor.fetchall()

    if not rows:
        print("No saved passwords.")

    else:
        for row in rows:

            decrypted_password = cipher.decrypt(
                row[2].encode()
            ).decode()

            print(f"""
=====================App: {row[0]}
Username: {row[1]}
Password: {decrypted_password}""")

elif command == "delete":

    if len(sys.argv) < 3:
        print("Usage: python3 r2.py delete <app1> <app2> ...")
        sys.exit()

    apps = sys.argv[2:]
    deleted = 0

    for app in apps:
        cursor.execute(
            "DELETE FROM accounts WHERE app = ?",
            (app,)
        )

        if cursor.rowcount > 0:
            print(f"[+] Deleted: {app}")
            deleted += 1
        else:
            print(f"[-] Not found: {app}")

    conn.commit()

    print(f"\n[+] Total deleted: {deleted}")

elif command == "ui":
    from tui import launch
    launch()


else:
    print("Unknown command!")

conn.close()