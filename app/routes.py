import re

from app import app, db
from app.forms import Registration, LogIn
from app.models import User

from flask import render_template, request, redirect, url_for, flash


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/registration", methods=["POST", "GET"])
def registration():
    form = Registration()

    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash("that username has been taken", 'alert alert-danger')
            return render_template("/forms/signup.html", form=form)
        elif User.query.filter_by(email=form.email.data).first():
            flash("that email has been taken", 'alert alert-danger')
            return render_template("/forms/signup.html", form=form)
        else:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('home'))

    return render_template("/forms/signup.html", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LogIn()

    if form.validate_on_submit():
        regex = re.compile(r"\w+@\w+\.\w+")
        if regex.search(form.email_or_username.data):
            user = User.query.filter_by(email=form.email_or_username.data).first()
            if user:
                if user.check_password(password=form.password.data):
                    flash("Nice")
                    return render_template("/forms/signin.html", form=form)
            else:
                flash("that user is not exists")
                return render_template("/forms/signin.html", form=form)
        else:
            user = User.query.filter_by(username=form.email_or_username.data).first()
            if user:
                if user.check_password(password=form.password.data):
                    flash("Nice")
                    return render_template("/forms/signin.html", form=form)
            else:
                flash("that user is not exists")
                return render_template("/forms/signin.html", form=form)
    return render_template("/forms/signin.html", form=form)