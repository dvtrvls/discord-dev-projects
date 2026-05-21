
# helper module
import os
import sys
import sqlite3
from cryptography.fernet import Fernet

# for output
from rich.console import Console 
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box

# for input
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML
from  prompt_toolkit.styles import Style


def get_app_dir():
    if sys.platform == "win32":
        base = os.getenv("APPDATA")
    else:
        base = os.getenv("XDG_DATA_HOME", os.path.join(os.path.expanduser("~"), ".local", "share"))
    return os.path.join(base, "RinLock")

APP_DIR = get_app_dir()
KEY_PATH = os.path.join(APP_DIR, "secret.key")
DB_PATH = os.path.join(APP_DIR, "rinlock.db")

def load_cipher():
    if not os.path.exists(KEY_PATH):
        return None
    with open(KEY_PATH, "rb") as file:
        return Fernet(file.read())

def get_master_password(conn):
    row = conn.execute("SELECT master_password FROM settings").fetchone()
    return row[0] if row else None

def fetch_accounts(conn, cipher):
    rows = conn.execute("SELECT id, app, username, password FROM accounts").fetchall()
    result = []
    for  row in rows:
        try: 
            decrypted = cipher.decrypt(row[3].encode()).decode()
        except Exception:
            decrypted = "[decryption error]"
        result.append({"id": row[0], "app": row[1], "username": row[2], "password": decrypted})
    return result

def delete_account(conn, account_id):
    conn.execute("DELETE FROM accounts WHERE id = ?", (account_id,))
    conn.commit()


console = Console()

BANNER =  r"""
 ____  _       _               _    
|  _ \(_)_ __ | |    ___   ___| | __
| |_) | | '_ \| |   / _ \ / __| |/ /
|  _ <| | | | | |__| (_) | (__|   < 
|_| \_\_|_| |_|_____\___/ \___|_|\_\
"""

ACCENT   = "bold cyan"
DIM      = "dim white"
DANGER   = "bold red"
SAFE     = "bold green"
NEUTRAL  = "bold white"
BOX_STYLE = box.DOUBLE_EDGE


def clear():
    console.clear()


prompt_style = Style.from_dict({
    "prompt": "bold cyan",
})
 

def render_banner():
    console.print(Text(BANNER, style="bold cyan"), justify="center")
    console.print(Align.center(Text("v2.0 - your passwords, your terminal", style=DIM)))
    console.print()

def render_status(msg: str, kind: str = "info"):
    color = {"info":ACCENT, "ok":SAFE, "err":DANGER}.get(kind, NEUTRAL)
    console.print(f"    [{color}]{msg}[/{color}]")
    console.print()

def render_footer(hints: list[str]):
    hint_text = "   ".join(f"[bold cyan]{k}[/bold cyan] {v}" for k,v in (h.split(" ", 1) for h in hints))
    console.rule(style="dim cyan")
    console.print(f"    {hint_text}", justify="left")


def screen_login(conn) -> bool: # pass connection
    clear()
    render_banner()
    saved = get_master_password(conn) # get the master passwowrd through the function that also uses the conn
    if not saved: # if there is no master password
        render_status("No master password set. Use: python3 r2.py setpass <password>", "err")
        input(" Press any key to exit ...")
        return False
    
    try: # ask the user to enter the master password
        entered = prompt(
            HTML("<prompt> Master password: </prompt>"),
            is_password=True,
            style=prompt_style
        )
    except (KeyboardInterrupt, EOFError):
        return False
    if entered != saved:
        clear()
        render_banner()
        render_status("Wrong master password. Access denied", "err")
        input("   Press any key to exit ...")
        return False
    return True


def screen_vault(conn, cipher):
    selected = 0
    reveal_set = set() #set of indices, maybe the for the accounts lists
    status_msg = ("", "info")
  

    def accounts():
        return fetch_accounts(conn, cipher) # returb lists of accounts (dict obj)

    while True:
        rows = accounts()
        clear()
        render_banner()

        if status_msg[0]:
            render_status(*status_msg)
            status_msg = ("", "info")

        if not rows:
            console.print(
                Panel(
                    Align.center(Text("No accounts saved yet.\n Use: python3 r2.py add <app> <user> <pass>", style=DIM)),
                    border_style="dim cyan",
                    padding=(1,4)
                )
            )
            render_footer(["q quit"])

            try:
                cmd = prompt(HTML("<cyan>  › </cyan>"), style=prompt_style).strip().lower()
            except (KeyboardInterrupt, EOFError):
                cmd = "q"
            if cmd == "q":
                break 
            continue
        selected = max(0, min(selected, len(rows)-1))

        table = Table(
            box=BOX_STYLE,
            border_style= "cyan",
            header_style="bold cyan",
            show_lines=True,
            expand=True
        )

        table.add_column("#",        style=DIM,     width=4,  justify="center")
        table.add_column("App",      style=NEUTRAL,  min_width=14)
        table.add_column("Username", style=NEUTRAL,  min_width=18)
        table.add_column("Password", min_width=22)

        for i, acc in enumerate(rows):
            is_selected = i == selected
            row_style = "on grey15" if is_selected else ""
            selector = "▶" if is_selected else " "

            if i in reveal_set:
                pw_text = Text(acc["password"], style=SAFE)
            else:
                pw_text = Text("•" * min(len(acc["password"]), 12), style=DIM)

            table.add_row(f"{selector}  {i+1}",
                          acc["app"],
                          acc["username"],
                          pw_text,
                          style=row_style)
        console.print(table)
        console.print()

        render_footer([
            "s ↓ navigate",
            "w ↑ navigate",
            "v reveal/hide",
            "d delete",
            "q quit",
        ])


        try:
            cmd = prompt(HTML("<cyan>  › </cyan>"), style=prompt_style).strip().lower()
        except (KeyboardInterrupt, EOFError):
            break
    
        if cmd in ("q", "quit", "exit"):
            break
        elif cmd in ("k", "up", "w"):
            selected = max(0, selected-1) 
        elif cmd in ("j", "down", "s"):
            selected = min(len(rows)-1, selected+1)
        elif cmd == "v":
            if selected in reveal_set:
                reveal_set.discard(selected)
            else:

                reveal_set.add(selected)
        elif cmd == "d":
            acc = rows[selected]
            clear()
            render_banner()
            console.print(
                Panel(
                    f"  [bold white]App:[/bold white]      {acc['app']}\n"
                    f"  [bold white]Username:[/bold white] {acc['username']}",
                    title="[bold red]Delete Account[/bold red]",
                    border_style="red",
                    padding=(1, 2),
                )
            )
            try: 
                confirm = prompt(HTML("<red>  Are you Sure? Type <b>yes</b> to confirm: </red>"),style=prompt_style).strip().lower()
            except (KeyboardInterrupt, EOFError):
                confirm = ""

            if confirm == "yes":
                delete_account(conn, acc["id"])
                reveal_set.discard(selected)
                selected = max(0, selected-1)
                status_msg = (f"Deleted '{acc['app']}' ({acc['username']}).", "ok")
            else:
                status_msg = ("Deletion cancelled.", "info")

        else:
            status_msg = (f"Unknown key '{cmd}'. Use w for ↑/ s for ↓ / v / d / q.", "info")

def screen_goodbye():
    clear()
    render_banner()
    console.print(Align.center(Text("Vault locked. Stay safe. 🔒", style="bold cyan")))
    console.print()


def launch():
    if not os.path.exists(DB_PATH):
        console.print(f"[bold red] Database not found at: [/bold red] {DB_PATH}")
        console.print("Run [bold cyan]python3 r2.py setpass <password>[/bold cyan] first.")
        sys.exit(1)

    cipher = load_cipher()
    if not cipher:
        console.print("[bold red]Encryption key not found.[/bold red] Cannot decrypt passwords.")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)

    try:
        if screen_login(conn):
            screen_vault(conn, cipher)
            screen_goodbye()
    finally:
        conn.close()

if __name__ == "__main__":
    launch()

