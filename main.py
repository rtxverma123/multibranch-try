from flask import Flask, render_template

app = Flask(__name__)

@app.route("/basic")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/")
def blog():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5000, debug="true")