import sqlite3
import time
from cryptography.fernet import Fernet
import re

class RinVault:
    def __init__(self):
        try:
            with open("secret.key", "rb") as key_file:
                self.key = key_file.read()
        except FileNotFoundError:
            self.key = Fernet.generate_key()
            with open("secret.key", "wb") as key_file:
                key_file.write(self.key)

        self.cipher = Fernet(self.key)

        print("""
██████╗░██╗███╗░░██╗░░░░░░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║████╗░██║░░░░░░██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
██████╔╝██║██╔██╗██║█████╗██║░░░░░██║░░██║██║░░╚═╝█████═╝░
██╔══██╗██║██║╚████║╚════╝██║░░░░░██║░░██║██║░░██╗██╔═██╗░
██║░░██║██║██║░╚███║░░░░░░███████╗╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░░░░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝
     A safe place to write and save your notes.""")
        time.sleep(1)

        self.conn = sqlite3.connect("Rin.db")
        self.cursor = self.conn.cursor()
        self.current_user_id = None
        
        self.custom_codes = {}
        
        self.setup_db()

    def setup_db(self):
        self.cursor.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        );

        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            app TEXT,
            username TEXT,
            password TEXT
        );

        CREATE TABLE IF NOT EXISTS mynotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    
        CREATE TABLE IF NOT EXISTS custom_commands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            command_key TEXT,
            action TEXT
        );
        """)
        
        self.conn.commit()

    def register(self):
        print("""
█▀█ █▀▀ █▀▀ █ █▀ ▀█▀ █▀▀ █▀█
█▀▄ ██▄ █▄█ █ ▄█ ░█░ ██▄ █▀▄""")

        username = input("\nCreate username: ")
        if username.lower() == "exit":
            return

        password = input("Create password: ")
        if password.lower() == "exit":
            return

        try:
            self.cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            self.conn.commit()
            print("\nAccount created successfully!")
        except sqlite3.IntegrityError:
            print("\nUsername already exists!")

    def login(self, username, password):
        print("""
█░░ █▀█ █▀▀ █ █▄░█
█▄▄ █▄█ █▄█ █ █░▀█""")

        self.cursor.execute(
            "SELECT id FROM users WHERE username = ? AND password = ?",
            (username, password)
        )

        user = self.cursor.fetchone()

        if user:
            self.current_user_id = user[0]
            print(f"\nWelcome Back!, {username}!")
            self.dashboard()
        else:
            print("\nInvalid username or password!")

    def add_note(self, title, notes):
        self.cursor.execute(
            "INSERT INTO mynotes (user_id, title, notes) VALUES (?, ?, ?)",
            (self.current_user_id, title, notes)
        )
        self.conn.commit()
        print("\nNote saved!")

    def view_notes(self):
        self.cursor.execute(
            "SELECT * FROM mynotes WHERE user_id = ?",
            (self.current_user_id,)
        )
        rows = self.cursor.fetchall()

        if not rows:
            print("No notes found.")
            return

        for row in rows:
            print(f"""
=====================
Title: {row[2]}
Note: {row[3]}
Created: {row[4]}
""")

    def edit_note(self):
        self.view_notes()

        title = input("\nEnter note title to edit: ")
        new_title = input("Enter new title: ")
        new_note = input("Enter new content: ")

        self.cursor.execute(
            """UPDATE mynotes SET title = ?, notes = ? WHERE title = ? AND user_id = ?""",
            (new_title, new_note, title, self.current_user_id)
        )

        self.conn.commit()

        if self.cursor.rowcount > 0:
            print("\nNote updated!")
        else:
            print("\nNote not found!")


    def del_note(self):
        self.view_notes()

        title = input("\nEnter note title to delete: ")

        self.cursor.execute(
            """DELETE FROM mynotes WHERE title = ? AND user_id = ?""",
            (title, self.current_user_id))

        self.conn.commit()

        if self.cursor.rowcount > 0:
            print("\nNote deleted!")
        else:
            print("\nNote not found!")

    def add_password(self, app, username, password):
        encrypted_password = self.cipher.encrypt(password.encode()).decode()
        self.cursor.execute(
            "INSERT INTO accounts (user_id, app, username, password) VALUES (?, ?, ?, ?)",
            (self.current_user_id, app, username, encrypted_password)
        )
        self.conn.commit()
        print("\nPassword saved!")

    def view_passwords(self):
        print("""
█▀ █░█ █▀█ █░█░█ █ █▄░█ █▀▀
▄█ █▀█ █▄█ ▀▄▀▄▀ █ █░▀█ █▄█""")
        time.sleep(1)

        self.cursor.execute(
            "SELECT app, username, password FROM accounts WHERE user_id = ?",
            (self.current_user_id,)
        )

        rows = self.cursor.fetchall()

        if not rows:
            print("No saved passwords.")
            return

        for row in rows:
            decrypted_password = self.cipher.decrypt(row[2].encode()).decode()

            print(f"""
=====================
App: {row[0]}
Username: {row[1]}
Password: {decrypted_password}""")

    def del_password(self):
        print("""
█▀█ █▀▀ █▀▄▀█ █▀█ █░█ █▀▀
█▀▄ ██▄ █░▀░█ █▄█ ▀▄▀ ██▄""")
            
        app = input("\nEnter app name to delete: ")
        self.cursor.execute(
            "DELETE FROM accounts WHERE app = ?",
            (app,)
        )
        self.conn.commit()
    
        time.sleep(1)
        print("\nPassword deleted!")
    
    def dashboard(self):
        while True:
            choice = input("""
[1] Add Note
[2] View Notes
[3] Edit Note
[4] Delete Note
[5] Logout

Choice: """)

            if choice == "1":
                title = input("Enter the title: ")
                notes = input("Enter the content: ")
                self.add_note(title, notes)

            elif choice == "2":
                self.view_notes()
                
            elif choice == "3":
                self.edit_note()

            elif choice == "4":
                self.del_note()

            elif choice == "5":
                self.current_user_id = None
                print("\nLogging out...\n")
                break
            elif choice == "RinLock_cmd":
                if not self.custom_codes:
                    print("No custom command set yet.")

                else:
                    print("""
============================
YOUR CUSTOM RINLOCK COMMANDS
============================
            """)

                for key, value in self.custom_codes.items():
                    print(f"{key} -> {value}")
        
            elif choice == "CODE2":
                print("""
==================================================
To see your command type: RinLock_cmd to dashboard

Format:
COMMAND1:add COMMAND2:view COMMAND3:delete
==================================================
            """)

                raw = input("\nEnter your secret commands: ").strip()

                if raw.lower() == "return":
                    print("Returning to dashboard...")
                    continue   # stays in dashboard loop

                pattern = r"(\w+):(\w+)\s+(\w+):(\w+)\s+(\w+):(\w+)"
                match = re.fullmatch(pattern, raw)

                if not match:
                    print("Invalid format!")
                    continue

                k1, v1, k2, v2, k3, v3 = match.groups()

                valid_actions = ["add", "view", "delete"]

                if v1 not in valid_actions or v2 not in valid_actions or v3 not in valid_actions:
                    print("Invalid command values!")
                    continue

                self.custom_codes = {
                    k1.strip(): v1.strip(),
                    k2.strip(): v2.strip(),
                    k3.strip(): v3.strip()
                }

                print("Commands saved successfully!")
                continue
            elif choice in self.custom_codes:
                action = self.custom_codes[choice].strip().lower()

                if action == "add":
                    app = input("App: ")
                    username = input("Username: ")
                    password = input("Password: ")
                    self.add_password(app, username, password)

                elif action == "view":
                    self.view_passwords()

                elif action == "delete":
                    self.del_password()

                else:
                    print("Invalid choice")

    def run(self):
        while True:
            usr_input = input("""
[1] Register
[2] Login
[3] Exit

Enter your choice: """)

            if usr_input == "1":
                print("\ntype: (exit) to return to menu")
                self.register()

            elif usr_input == "2":
                username = input("Enter your registered username: ")
                password = input("Enter your password: ")
                self.login(username, password)

            elif usr_input == "3":
                time.sleep(1)
                print("\nGoodbye!..")
                time.sleep(1)
                print("U wasted my time!.")
                break
            
            else:
                print("\nInvalid choice!")

        self.conn.close()

if __name__ == "__main__":
    app = RinVault()
    app.run()