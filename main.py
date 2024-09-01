from flask import Flask

from routes.login import login
from routes.signup import signup
from routes.index import index
from socketio_seteup.socketio_setup import socketio
from db.database import db
from routes.login import login_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# configure the SQLite db, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
login_manager.init_app(app)

with app.app_context():
    db.create_all()


socketio.init_app(app)

app.register_blueprint(login)
app.register_blueprint(signup)
app.register_blueprint(index)

if __name__ == '__main__':
    app.run(debug=True)
