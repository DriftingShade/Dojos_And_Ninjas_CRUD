from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/dojo_info/<int:dojo_id>")
def get_ninjas(dojo_id):
    ninjas = Ninja.get_dojo_ninjas({"dojo_id": dojo_id})
    return render_template("dojo_show.html", ninjas=ninjas)


@app.route("/ninja_page")
def ninja_page(dojo_id):
    return render_template("new_ninja.html", dojo_id=dojo_id)

@app.post("/create_ninja")
def new_ninja():
    ninja_info = {
        "dojo_id": request.form["dojo_id"]
    }