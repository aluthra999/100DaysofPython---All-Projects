from flask import Flask, render_template, request
import requests
import datetime
import smtplib

my_email = ""
app_password = ""

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


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    current_year = datetime.datetime.now().year
    if request.method == 'GET':
        display_text = "Contact Me"
        return render_template("contact.html", year=current_year, h1=display_text)
    elif request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        if name and email and phone and message:
            print(f"{name}\n{email}\n{phone}\n{message}")
            success_text = "Successfully sent your message"
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(
                    user=my_email,
                    password=app_password
                )
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=my_email,
                    msg=f"Subject:New message from {name} on Blog Site\n\n{name}\n{email}\n{phone}\n{message}"
                )
            return render_template("contact.html", h1=success_text)
        else:
            return "<h1>Please fill out all the details</h1"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    current_year = datetime.datetime.now().year
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=current_year)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

