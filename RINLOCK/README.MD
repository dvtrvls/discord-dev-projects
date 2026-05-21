# RinVault

A simple terminal-based password and notes manager built with Python and SQLite.

---

# Features

- User registration and login
- User-specific notes
- Password manager
- Secret custom commands
- SQLite database support
- Terminal-based interface
- Edit notes
- Delete notes
- Delete passwords

---

# Requirements

- Python 3 installed

Check if Python is installed:

```bash
python --version
```

or

```bash
python3 --version
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/RinVault.git
```

Go to the project folder:

```bash
cd RinVault
```

---

# Running The Program

Run the program using:

```bash
python3 rinlock.py
```

or on Windows:

```bash
python rinlock.py
```

---

# Main Menu

When the program starts, you will see:

```text
[1] Register
[2] Login
[3] Exit
```

---

# Creating An Account

Press:

```text
1
```

Then enter:

```text
Create username:
Create password:
```

Example:

```text
Create username: Jhon
Create password: Rain123
```

---

# Logging In

Press:

```text
2
```

Then enter your account credentials:

```text
Enter your registered username:
Enter your password:
```

---

# Dashboard Menu

After logging in:

```text
[1] Add Note
[2] View Notes
[3] Edit Note
[4] Delete Note
[5] Logout
```

---


# Secret Password Commands

Inside the dashboard, type:

```text
CODE2
```

You will see:

```text
Format: COMMAND1:add COMMAND2:view COMMAND3:delete
```

Then enter your custom commands:

```text
Enter your secret commands:
```

Example:

```text
MYADD:add MYVIEW:view MYDELETE:delete
```

---

# Using Secret Commands

## Add Password

Use your custom add command.

Example:

```text
MYADD
```

Then enter:

Example:

```text
App: Facebook
Username: jhon123
Password: mypassword
```

---

## View Passwords

Use your custom view command.

Example:

```text
MYVIEW
```

---

## Delete Passwords

Use your custom delete command.

Example:

```text
MYDELETE
```

Then enter:

```text
Enter app name to delete:
```

---

# Database

The program automatically creates:

```text
Rin.db
```

This database stores:
- users
- notes
- passwords

---

# Project Structure

```text
RINLOCK/
│
├── rinlock.py
├── Rin.db
└── README.md
```

---

# Warning

Do not use for highly sensitive data.

---

# Author

Developed by Jhon Aldrix
