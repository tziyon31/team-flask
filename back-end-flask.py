from flask import Flask, request, render_template

app = Flask(__name__)
    
@app.route('/<room>')
def room(room):
        return render_template('index.html', room=room)
@app.route('/api/chat/<room>', methods=['POST'])
def chat(room):
        



if __name__ == '__main__':
    app.run(debug=True)