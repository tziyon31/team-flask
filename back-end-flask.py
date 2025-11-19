from flask import Flask, request, render_template 
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


# Person B
@app.route('/api/chat/<room>', methods=['POST'])
def chat(room):
    return "Hello, World!"

# Person A - Implemented by Judith
@app.route('/api/chat/<room>', methods=['GET'])
def get_chat(room):
    filename = f"chat_{room}.txt"

    # אם אין קובץ – הצ'אט ריק
    if not os.path.exists(filename):
        return "", 200

    # אם יש קובץ – קוראים את כולו
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    return content, 200

if __name__ == '__main__':
    app.run(debug=True)
