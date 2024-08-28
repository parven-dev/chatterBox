from flask import Flask

from routes.login import login
from routes.signup import signup


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# configure the SQLite db, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

app.register_blueprint(login)
app.register_blueprint(signup)

if __name__ == '__main__':
    app.run(debug=True)
