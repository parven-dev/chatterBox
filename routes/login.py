from flask import Blueprint, render_template, request, redirect, url_for
from db.database import User

login = Blueprint("login", __name__, url_prefix="/login")


@login.route("/", methods=["GET", "POST"])
def login_view():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pass"]
        user = User.query.filter_by(email=email).first()
        if user and password == user.password:
            return "you login successfully"
        # Perform login logic here
        else:
            return redirect(url_for("login.login_view"))
    return render_template("login.html")
