import sqlite3
import time


class RinVault:
    def __init__(self):
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
Title: {row[2]}
Note: {row[3]}
Created: {row[4]}
""")

    def add_password(self, app, username, password):
        self.cursor.execute(
            "INSERT INTO accounts (user_id, app, username, password) VALUES (?, ?, ?, ?)",
            (self.current_user_id, app, username, password)
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
            print(f"""
=====================
App: {row[0]}
Username: {row[1]}
Password: {row[2]}
""")

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
[3] Logout

Choice: """)

            if choice == "1":
                title = input("Enter the title: ")
                notes = input("Enter the content: ")
                self.add_note(title, notes)

            elif choice == "2":
                self.view_notes()

            elif choice == "CODE2":
                print("""
Format: COMMAND1:add COMMAND2:view COMMAND3:delete
            """)

                mappings = input("Enter your secret commands: ").split()

                for item in mappings:
                    key, value = item.split(":")
                    self.custom_codes[key] = value

                print("Commands saved!")

            elif choice in self.custom_codes:
                action = self.custom_codes[choice]

                if action == "add":
                    app = input("App: ")
                    username = input("Username: ")
                    password = input("Password: ")
                    self.add_password(app, username, password)

                elif action == "view":
                    self.view_passwords()

                elif action == "delete":
                    self.del_password()

            elif choice == "3":
                self.current_user_id = None
                print("\nLogging out...\n")
                break

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