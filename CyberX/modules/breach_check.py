import requests
from rich.console import Console

console = Console()

def check_breach(email):
    console.print(f"\n[bold green]🔍 Checking breaches for:[/bold green] {email}")
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": "YOUR_API_KEY", "user-agent": "CyberX-Terminal"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        breaches = response.json()
        console.print(f"[bold red]⚠️ Found {len(breaches)} breaches![/bold red]")
        with open("results/breaches.txt", "w") as f:
            for breach in breaches:
                console.print(f"[bold yellow]- {breach['Name']}[/bold yellow]")
                f.write(f"{breach['Name']}\n")
    elif response.status_code == 404:
        console.print("[bold green]✅ No breaches found![/bold green]")
    else:
        console.print("[bold yellow]⚠️ API Error or Rate Limited[/bold yellow]")
