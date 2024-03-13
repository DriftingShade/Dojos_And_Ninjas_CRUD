from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    all_dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos=all_dojos)

@app.post("/create_dojo")
def create_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect("/")