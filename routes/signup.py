from flask import render_template, request, Blueprint
# from db.database import User

signup = Blueprint('signup', __name__, url_prefix="/signup")


@signup.route("/", methods=["GET", "POST"])
def signup_view():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pass"]
        # print(email, password)
        # user = User(
        #     email=email,
        #     password=password
        # )
        #
        # db.session.add(user)
        # db.session.commit()
        # return "success"

    return render_template("/signup.html")
