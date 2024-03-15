from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/dojo_info/<int:id>")
def get_ninjas(id):
    data = {
        "id": id
    }
    return render_template("dojo_show.html", dojo = Dojo.get_one(data))


@app.route("/ninja_page")
def ninja_page():
    all_dojos = Dojo.get_all()
    return render_template("new_ninja.html", all_dojos=all_dojos)

@app.post("/create_ninja")
def new_ninja():
    dojo_id = request.form["dojo_id"]
    Ninja.save(request.form)
    return redirect(f"/dojo_info/{dojo_id}")

@app.get("/edit_ninja/<int:ninja_id>")
def edit_ninja(ninja_id):
    ninja = Ninja.find_by_id({"id": ninja_id})
    if ninja == None:
        return "Cannot find Ninja."
    return render_template("edit_ninja.html", ninja=ninja)

@app.post("/update_ninja")
def update_ninja():
    dojo_id = request.form["dojo_id"]
    Ninja.update(request.form)
    return redirect(f"/dojo_info/{dojo_id}")

@app.post("/delete_ninja/<int:ninja_id>")
def delete_ninja(ninja_id):
    dojo_id = request.form["dojo_id"]
    Ninja.delete(ninja_id)
    return redirect(f"/dojo_info/{dojo_id}")
