from flask import render_template, request, Blueprint, redirect
from db.database import User, db

signup = Blueprint('signup', __name__, url_prefix="/signup")


@signup.route("/", methods=["GET", "POST"])
def signup_view():
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
        return redirect('/index.html')

    return render_template("/signup.html")
