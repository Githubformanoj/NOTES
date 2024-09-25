from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

# Adding a dynamic route below.

@app.route("/<name>")
def dynamic(name):
    return f"Hello {name}"

if __name__ == '__main__':
    app.run()