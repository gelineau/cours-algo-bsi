from flask import Flask, render_template, request, redirect, url_for, make_response
from functools import wraps
import model

app = Flask(__name__)


def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = request.cookies.get("username")
        if not username:
            return redirect(url_for("login_controller"))
        return f(*args, **kwargs)

    return decorated_function


@app.route("/", methods=["GET"])
def index_controller() -> str:
    return render_template("index.html")


@app.route("/hello", methods=["GET"])
def hello_controller() -> str:
    return render_template("hello.html")


@app.route("/greet/<int:age>", methods=["GET"])
def greet_controller(age: int) -> str:
    if age < 18:
        return render_template("child.html", age=age)
    return render_template("adult.html", age=age)


@app.route("/users", methods=["GET"])
@require_login
def users_controller() -> str:
    users = model.get_users()
    return render_template("users.html", users=users)


@app.route("/user_form", methods=["GET"])
@require_login
def user_form_controller() -> str:
    return render_template("user_form.html")


@app.route("/create_user", methods=["POST"])
@require_login
def create_user_controller() -> str:
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    model.create_user(username, email, password)
    return render_template("create_user.html", username=username)


@app.route("/login", methods=["GET"])
def login_controller() -> str:
    return render_template("login.html")


@app.route("/do_login", methods=["POST"])
def do_login_controller() -> str:
    username = request.form["username"]
    password = request.form["password"]

    if model.check_user_credentials(username, password):
        response = make_response(
            render_template("login_success.html", username=username)
        )
        response.set_cookie("username", username)
        return response
    return render_template("login_fail.html")


if __name__ == "__main__":
    app.run(debug=True)
