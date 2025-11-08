# password-security-demo

This repo demonstrates common security pitfalls and defenses using **safe, local-only** targets:
- A **demo “bank” server** for measuring dictionary attacks
- A **phishing UI** with credential capture + keystroke logging (localhost only)

**Ethics:** For learning on localhost only. Do not scan or attack real systems without explicit permission.

## What’s Included
- `demo_target/server.py` — Flask app that emulates a login endpoint for testing
- `attacks/dictionary_attack.py` — small dictionary attack against the demo target
- `phishing-demo/app.py` — phishing login page + keystroke capture; view data at `/manage`
- `wordlists/small.txt` — tiny test list
- `requirements.txt` — Flask + requests

