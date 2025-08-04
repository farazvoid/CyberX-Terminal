# CyberX-Terminal
CyberX Terminal – Next-Gen OSINT Toolkit CyberX Terminal is a flashy, hacker-style Python tool designed for ethical hackers, penetration testers, and cybersecurity enthusiasts. It brings two powerful reconnaissance features into one futuristic terminal environment, making information gathering faster, easier, and visually impressive.
🛠️ What is CyberX Terminal?
CyberX Terminal is a flashy hacker-style Python tool designed to combine two powerful OSINT features in one place:

Sherlock Username Lookup

Searches a given username across hundreds of websites.

Helps you find where a username is registered online.

Useful for recon and footprinting in ethical hacking.

HaveIBeenPwned Email Breach Checker

Checks if an email appears in known data breaches or leaks.

Lets you know if an account was compromised in past hacks.

Uses the official HaveIBeenPwned API, requiring a free API key.

⚡ How It Works
Step 1: The user opens CyberX Terminal.

Step 2: The terminal shows a hacker-style neon banner with menu options:

1 → Username Lookup (Sherlock)

2 → Email Breach Check (HaveIBeenPwned)

3 → Run Both

4 → Exit

Step 3: The tool performs the scan and saves results in /results/ folder.

Step 4: Users can analyze where their usernames are found or if their emails are leaked.

🔑 Using Your Own HaveIBeenPwned API Key
CyberX Terminal does not provide a public API key.
You must use your own key to stay secure and respect API limits.

How to Get an API Key:
Go to https://haveibeenpwned.com/API/Key

Sign up or log in.

Get your personal API key (usually a long alphanumeric string).

Where to Add Your Key in CyberX
In breach_check.py, replace:

python
Copy
Edit
headers = {"hibp-api-key": "YOUR_API_KEY", "user-agent": "CyberX-Terminal"}
With:

python
Copy
Edit
headers = {"hibp-api-key": "PUT-YOUR-API-KEY-HERE", "user-agent": "CyberX-Terminal"}
📜 Usage Disclaimer (You Should Tell People)
When sharing CyberX Terminal, include a README message:

⚠️ Disclaimer:

This tool is for educational and ethical hacking purposes only.

Do not use CyberX Terminal to target accounts that do not belong to you.

Each user must provide their own HaveIBeenPwned API key.

Misuse of this tool is illegal and the creator is not responsible for damages caused by unethical use.
