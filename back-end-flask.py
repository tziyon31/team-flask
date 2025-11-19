from flask import Flask, request, render_template
from datetime import datetime
import os

app = Flask(__name__)

# Person A - Implemented by Judith
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Person B
@app.route('/<room>')
def room(room):
    return render_template('index.html', room=room)

@app.route('/api/chat/<room>', methods=['POST'])
def chat(room):
    username = request.form.get('username')
    msg = request.form.get('msg')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"{timestamp}  {username}: {msg} "
    filename = f"chat_{room}.txt"
    with open(filename, "a", encoding='utf-8') as f:
        f.write(message + "\n")
    return "", 204

# Person A - Implemented by Judith
@app.route('/api/chat/<room>', methods=['GET'])
def get_chat(room):
    filename = f"chat_{room}.txt"
    if not os.path.exists(filename):
        return "", 200
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    return content, 200

if __name__ == '__main__':
    app.run(debug=True)
