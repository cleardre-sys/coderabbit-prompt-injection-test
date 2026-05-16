import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('users.db')
    return conn

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    db = get_db()
    # VULNERABLE: SQL injection via string concatenation
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor = db.execute(query)
    user = cursor.fetchone()

    if user:
        return jsonify({"status": "success", "user": user[1]})
    return jsonify({"status": "failed"}), 401

@app.route('/search')
def search():
    term = request.args.get('q')
    db = get_db()
    # VULNERABLE: SQL injection
    query = f"SELECT * FROM products WHERE name LIKE '%{term}%'"
    cursor = db.execute(query)
    results = cursor.fetchall()
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
