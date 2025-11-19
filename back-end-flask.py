from flask import Flask, render_template

app = Flask(__name__)

# Person A - Implemented by Judith
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
