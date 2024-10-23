from flask import render_template, redirect, request, url_for
from . import app, db
from .models import Task, User
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, login_required, UserMixin, logout_user, current_user


login_manager = LoginManager(app)
login_manager.login_view = 'auth'

app.config["SECRET_KEY"] = "jr134244a"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

bcrypt = Bcrypt(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        add_task = Task(task=request.form.get("task"))
        db.session.add(add_task)
        db.session.commit()
        return redirect(url_for("home"))

    todos = Task.query.all()
    return render_template("index.html", todos=todos)


@app.route("/auth", methods=["GET", "POST"])
def auth():
    form_type = request.args.get("form_type")
    if request.method == "POST":
        if form_type == "login":
            username = request.form.get("username")
            password = request.form.get("password")
            return redirect(url_for("home"))
        if form_type == "register":
            name = request.form.get("name")
            email = request.form.get("email")
            username = request.form.get("username")
            password = request.form.get("password")
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            
            new_user = User(name=name, email=email, username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("dashboard"))

    form_type = request.args.get("form", "login")    
    return render_template("auth.html", form_type = form_type)


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)