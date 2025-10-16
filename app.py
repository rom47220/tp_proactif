from flask import Flask, request, render_template
import os
import sqlite3

app = Flask(__name__)

# Vulnérabilité 1 : Injection SQL
def get_user_from_db(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"  # ❌ injection volontaire
    c.execute(query)
    return c.fetchall()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    username = request.args.get("user")
    results = get_user_from_db(username)
    return f"Résultats pour {username}: {results}"

# Vulnérabilité 2 : Commande système
@app.route("/ping")
def ping():
    host = request.args.get("host")
    return os.popen(f"ping -c 1 {host}").read()  # ❌ injection de commande

if __name__ == "__main__":
    app.run(debug=True)
