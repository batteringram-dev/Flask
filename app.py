from flask import Flask, redirect, url_for          # Redirecting functions

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is the main page."

@app.route("/<name>")
def user(name):                           # This function helps us in writing a name after the slash
    return f"Hello {name}!"

@app.route("/admin")
def admin():                              # Redirecting to the original page if the user gets to another page
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
