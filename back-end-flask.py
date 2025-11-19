from flask import Flask, request, render_template

app = Flask(__name__)

# Person A - Implemented by Judith
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


    @app.route('/<room>')
    def room(room):
        return render_template('index.html', room=room)

    @app.route('/api/chat/<room>', methods=['POST'])
    def chat(room):
        return "Hello, World!"
    if __name__ == '__main__':
          app.run(debug=True)

