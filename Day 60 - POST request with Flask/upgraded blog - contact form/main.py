from flask import Flask, render_template, request
import requests
import datetime

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/54544f573a81c8ef5e80").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    current_year = datetime.datetime.now().year
    return render_template("index.html", all_posts=posts, year=current_year)


@app.route("/about")
def about():
    current_year = datetime.datetime.now().year
    return render_template("about.html", year=current_year)


@app.route("/contact")
def contact():
    current_year = datetime.datetime.now().year
    return render_template("contact.html", year=current_year)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    current_year = datetime.datetime.now().year
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=current_year)


@app.route("/form-entry", methods=["POST"])
def receive_data():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")

    if name and email and phone and message:
        print(f"{name}\n{email}\n{phone}\n{message}")
        return "<h1>Successfully sent your message</h1>"
    else:
        return "<h1>Please fill out all the details</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5001)