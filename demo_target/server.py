from flask import Flask, request
app = Flask(__name__)

# Demo credentials (for local testing only)
DEMO_USER = "student"
DEMO_PASS = "husky123"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    # This response text mirrors the original lab behavior:
    # success: "Welcome!"  failure: includes "Wrong username"
    if username == DEMO_USER and password == DEMO_PASS:
        return "Welcome!"
    return "Wrong username or password."

@app.route("/")
def index():
    return "Demo Bank Target. POST to /login with form fields username/password."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
