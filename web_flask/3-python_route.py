#!/usr/bin/python3
"""
add new routes with flask
"""
from flask import Flask

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ display hello hbnb """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ display hbnb """
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c_with_txt(text):
    """ display text from the user """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/<string:text>", strict_slashes=False)
def python_with_txt(text):
    """ display text from the user """
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
