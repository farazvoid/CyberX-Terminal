import os
from rich.console import Console
from rich.progress import track

console = Console()

def sherlock_lookup(username):
    console.print(f"\n[bold green]🔍 Searching for username:[/bold green] {username}")
    os.system(f"python3 -m sherlock {username} --output results/usernames.txt")
    console.print("[bold cyan]✅ Scan complete! Results saved in results/usernames.txt[/bold cyan]")
#nothiing
