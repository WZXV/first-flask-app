from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class Registration(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=10)], render_kw={"placeholder": "username"})
    email = EmailField("email", validators=[DataRequired(), Email()], render_kw={"placeholder": "email"})
    password = PasswordField("password", validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "password"})
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "confirm password"})
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign up')


class LogIn(FlaskForm):
    email_or_username = StringField("email or username", validators=[DataRequired()], render_kw={"placeholder": "username or email"})
    password = PasswordField("password", validators=[DataRequired()], render_kw={"placeholder": "password"})
    submit = SubmitField("Sign in")