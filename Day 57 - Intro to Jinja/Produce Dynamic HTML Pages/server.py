from flask import Flask, render_template
import datetime
import random
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", number=random_number, year=current_year)


@app.route("/guess/<name>")
def api(name):
    agify = requests.get(url=f'https://api.agify.io?name={name}')
    age = agify.json()['age']

    genderize = requests.get(url=f"https://api.genderize.io?name={name}")
    gender = genderize.json()['gender']

    return render_template("api.html", name=name.title(), age=age, gender=gender)


@app.route('/blog')
def get_blog():
    blog_url = "https://www.npoint.io/docs/c790b4d5cab58020d391"
    response = requests.get(blog_url)

    if response.status_code == 200:
        try:
            all_posts = response.json()
        except ValueError:
            return "Failed to retrieve and parse blog data."

        return render_template("blog.html", posts=all_posts)
    else:
        return "Failed to retrieve blog data. Status code: " + str(response.status_code)


if __name__ == "__main__":
    app.run(debug=True)
