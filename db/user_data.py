
from main import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))

    # def __init__(self, email, password):
    #     self.email = email
    #     self.password = password


with app.app_context():
    db.create_all()