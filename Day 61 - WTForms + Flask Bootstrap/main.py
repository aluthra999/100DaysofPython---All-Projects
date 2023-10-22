from flask import Flask, render_template, request, redirect
from forms import LoginForm
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = "thiskeyisverysecret"
ADMIN_EMAIL = os.environ.get("FLASKWTForms_ADMIN_EMAIL")
ADMIN_PASSWORD = os.environ.get("FLASKWTForms_ADMIN_PASS")


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Check if the email and password match the admin credentials
        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            return redirect('/success')
        else:
            return redirect('/denied')

    return render_template('login.html', form=form)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/denied')
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
