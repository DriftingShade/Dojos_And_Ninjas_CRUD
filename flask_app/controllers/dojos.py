from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dashboard():
    return render_template('dojos.html', all_dojos = Dojo.get_all())


@app.post("/create_dojo")
def create_dojo():
    data = {"name": request.form["name"]}
    Dojo.save(data)
    return redirect("/")
