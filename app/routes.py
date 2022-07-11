import re

from app import app, db, login_manager
from app.forms import Registration, LogIn
from app.models import User

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/home")
@login_required
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
        user = User.query.filter_by(username=form.email_or_username.data).first()

        if user and user.check_password(form.password.data):

            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("home"))
        else:
            flash("Incorrect username or password", "alert alert-danger")
            return redirect(url_for("login"))


    return render_template("/forms/signin.html", form=form)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for('registration'))