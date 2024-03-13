from flask import Flask, render_template, request, redirect
from flask_app import app


@app.route("/")
def index():
    return render_template("dojos.html")


if __name__ == "__main__":
    app.run(debug=True)
