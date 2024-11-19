# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello World, from Flask!"

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "BIG MILKERS MMM"

if __name__ == "__main__":
    app.run(debug=True)
