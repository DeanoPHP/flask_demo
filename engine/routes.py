from flask import render_template, redirect, request, url_for
from . import app, db
from .models import Task

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        add_task = Task(task = request.form.get("task"))
        db.session.add(add_task)
        db.session.commit()
        return redirect(url_for("home"))
    
    todos = Task.query.all()
    return render_template("index.html", todos=todos)