from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/dojo_info/<int:dojo_id>")
def get_ninjas(dojo_id):
    ninjas = Ninja.get_dojo_ninjas({"dojo_id": dojo_id})
    return render_template("dojo_show.html", ninjas=ninjas)


@app.route("/ninja_page")
def ninja_page():
    all_dojos = Dojo.get_all()
    return render_template("new_ninja.html", all_dojos=all_dojos)

# @app.post("/create_ninja/<int:dojo_id>")
# def new_ninja(dojo_id):
#     ninja_info = {
#         "dojo_id": request.form["dojo_id"],
#         "first_name": request.form["first_name"],
#         "last_name": request.form["last_name"],
#         "age": request.form["age"]
#     }
#     Ninja.save(ninja_info)
#     return redirect("/dojo_info/<int:dojo_id>", dojo_id=dojo_id)