from flask import Flask, render_template, request
import model

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index_controller() -> str:
    return render_template('index.html')


@app.route('/hello', methods=['GET'])
def hello_controller() -> str:
    return render_template('hello.html')


@app.route('/greet/<int:age>', methods=['GET'])
def greet_controller(age: int) -> str:
    if age < 18:
        return render_template('child.html', age=age)
    return render_template('adult.html', age=age)


@app.route('/users', methods=['GET'])
def users_controller() -> str:
    users = model.get_users()
    return render_template('users.html', users=users)


@app.route('/user_form', methods=['GET'])
def user_form_controller() -> str:
    return render_template('user_form.html')


@app.route('/create_user', methods=['POST'])
def create_user_controller() -> str:
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    model.create_user(username, email, password)
    return render_template('create_user.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
