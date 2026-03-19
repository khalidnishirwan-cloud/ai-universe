import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
from flask import Flask, render_template, request, jsonify, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_message = data.get('message')

    # رد تجريبي
    response = f"أنت قلت: {user_message}"

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
