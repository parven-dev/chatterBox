from flask import Blueprint, render_template
from flask_socketio import emit

from socketio_seteup.socketio_setup import socketio

index = Blueprint("index", __name__, url_prefix="/")


@index.route('/')
def index_view():
    return render_template('index.html')


@socketio.on('message')
def handle_message(data):
    print('Received message: ' + data)
    emit('response', 'Server received your message: ' + data)


@socketio.on('json')
def handle_json(json):
    print('Received JSON: ' + str(json))
    emit('response', 'Server received your JSON: ' + str(json))
