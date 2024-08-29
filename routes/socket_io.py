
from flask import render_template
from flask_socketio import SocketIO, emit
from main import app


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





