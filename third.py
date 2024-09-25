from flask import Flask, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"


# How to redirect a url?

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))


if __name__ == '__main__':
    app.run(debug=True)