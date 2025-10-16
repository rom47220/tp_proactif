from flask import Flask, request, render_template
import os, subprocess
import sqlite3
from markupsafe import escape

app = Flask(__name__)

# Vulnérabilité 1 (fixé): Injection SQL
def get_user_from_db(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    c.execute(query, (username,))
    return c.fetchall()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    username = request.args.get("user", "")
    results = get_user_from_db(username)
    return f"Résultats pour {escape(username)}: {results}"


# Vulnérabilité 2 (fixé) : Commande système
@app.route("/ping")
def ping():
    host = request.args.get("host")
    result = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    app.run
