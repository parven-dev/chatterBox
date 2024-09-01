from flask import Blueprint, render_template, request, redirect, url_for
from db.database import User

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

login = Blueprint("login", __name__, url_prefix="/login")

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@login.route("/", methods=["GET", "POST"])
def login_view():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pass"]
        user = User.query.filter_by(email=email).first()
        if user and password == user.password:
            login_user(user)
            return "you login successfully"
        # Perform login logic here
        else:
            return redirect(url_for("login.login_view"))
    return render_template("login.html")
