from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import Length, DataRequired


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Length(max=30)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(max=30)])
    submit = SubmitField(label="Log In")
