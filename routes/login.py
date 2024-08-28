from flask import Blueprint, render_template, request, redirect, url_for

login = Blueprint("login", __name__, url_prefix="/login")

@login.route("/", methods=["GET", "POST"])
def login_view():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pass"]
        # Perform login logic here
        return redirect(url_for("login.login_view"))
    return render_template("login.html")
