from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/")
def index():
    all_dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos=all_dojos)


@app.post("/create_dojo")
def create_dojo():
    data = {"name": request.form["name"]}
    Dojo.save(data)
    return redirect("/")


@app.route("/dojo_info/<int:dojo_id>")
def get_ninjas(dojo_id):
    ninjas = Ninja.get_dojo_ninjas({"dojo_id": dojo_id})
    return render_template("dojo_show.html", ninjas=ninjas)


@app.route("/ninja_page")
def ninja_page():
    return render_template("new_ninja.html")
