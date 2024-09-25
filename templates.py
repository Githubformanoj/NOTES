from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/<name>')
# def user(name):
#     return render_template("index.html", content=["Cat","Dog",55])


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)


