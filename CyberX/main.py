import os
import time
from modules.sherlock_scan import sherlock_lookup
from modules.breach_check import check_breach
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()

def banner():
    with open("banner.txt", "r") as b:
        console.print(b.read(), style="bold magenta")

def menu():
    console.print("\n[bold cyan]1.[/bold cyan] Username Lookup (Sherlock)")
    console.print("[bold cyan]2.[/bold cyan] Email Breach Check (HaveIBeenPwned)")
    console.print("[bold cyan]3.[/bold cyan] Run Both")
    console.print("[bold cyan]4.[/bold cyan] Exit\n")
    return input("Choose an option: ")

def cyberx_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    banner()
    while True:
        choice = menu()
        if choice == "1":
            username = input("Enter username: ")
            sherlock_lookup(username)
        elif choice == "2":
            email = input("Enter email: ")
            check_breach(email)
        elif choice == "3":
            username = input("Enter username: ")
            email = input("Enter email: ")
            sherlock_lookup(username)
            check_breach(email)
        elif choice == "4":
            console.print("Exiting CyberX Terminal...", style="bold red")
            break
        else:
            console.print("Invalid choice!", style="bold yellow")

if __name__ == "__main__":
    cyberx_terminal()
