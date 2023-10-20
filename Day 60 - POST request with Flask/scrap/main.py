from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST"])
def receive_data():
    username = request.form.get("username")
    password = request.form.get("password")

    if username and password:
        return f"<h1>Username: {username}, Password: {password}</h1>"
    else:
        return "<h1>Username and/or Password not provided</h1>"


if __name__ == "__main__":
    app.run(debug=True)

