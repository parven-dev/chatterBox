from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(data):
    print('Received message: ' + data)
    emit('response', 'Server received your message: ' + data)


@socketio.on('json')
def handle_json(json):
    print('Received JSON: ' + str(json))
    emit('response', 'Server received your JSON: ' + str(json))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pass"]
        print(email, password)
    return render_template("/login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pass"]
        print(email, password)
    return render_template("/signup.html")


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
