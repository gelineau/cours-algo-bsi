from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True)


