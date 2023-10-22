from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators
from wtforms.validators import DataRequired, URL
import csv
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

current_year = datetime.now().year


class CafeForm(FlaskForm):
    hours_choices = [(str(i), f'{i}:00') for i in range(0, 24)]
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location (URL)', validators=[DataRequired(), URL(message="Invalid URL")])
    open_time = SelectField('Open Time', choices=hours_choices, validators=[DataRequired()])
    close_time = SelectField('Closing Time', choices=hours_choices, validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[(str(i), i) for i in range(6)], coerce=int,
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wi-Fi Rating', choices=[(str(i), i) for i in range(6)], coerce=int,
                              validators=[DataRequired()])
    power_rating = SelectField('Power Outlet Rating', choices=[(str(i), i) for i in range(6)], coerce=int,
                               validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, Wi-Fi rating, power outlet rating fields
# make coffee/Wi-Fi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html", year=current_year)


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([
                form.cafe.data,
                form.location.data,
                form.open_time.data,
                form.close_time.data,
                '☕' * form.coffee_rating.data,
                '💪' * form.wifi_rating.data,
                '🔌' * form.power_rating.data
            ])
            # Add a line break
            csv_file.write('\n')
        return redirect('/cafes')
    return render_template('add.html', form=form, year=current_year)


@app.route('/cafes')
def cafes():
    list_of_cafes = []
    with open('cafe-data.csv', 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            list_of_cafes.append(row)
    return render_template('cafes.html', cafes=list_of_cafes, year=current_year)


if __name__ == '__main__':
    app.run(debug=True)
