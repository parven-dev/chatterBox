from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# configure the SQLite db, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))

    # def __init__(self, email, password):
    #     self.email = email
    #     self.password = password


with app.app_context():
    db.create_all()


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
        user = User(
            email=email,
            password=password
        )

        db.session.add(user)
        db.session.commit()
        return "success"

    return render_template("/signup.html")


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
