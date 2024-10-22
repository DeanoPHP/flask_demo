from flask import render_template, redirect, request, url_for
from . import app, db
from .models import Task


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        add_task = Task(task=request.form.get("task"))
        db.session.add(add_task)
        db.session.commit()
        return redirect(url_for("home"))

    todos = Task.query.all()
    return render_template("index.html", todos=todos)

# here i want a route that handles show login
# form or register form when clicked


@app.route("/auth", methods=["GET", "POST"])
def auth():
    form_type = request.args.get("form", "login")
    if request.method == "POST":

        if form_type == "login":
            username = request.form.get("username")
            password = request.form.get("password")
            return redirect(url_for("dashboard"))
        if form_type == "register":
            username = request.form.get("username")
            password = request.form.get("password")
            return redirect(url_for("login"))
        
    return render_template("auth.html", form_type = form_type)