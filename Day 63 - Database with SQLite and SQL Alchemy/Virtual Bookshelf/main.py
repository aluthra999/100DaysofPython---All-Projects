from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_bootstrap import Bootstrap5
from datetime import datetime

app = Flask(__name__)
Bootstrap5(app)
current_year = datetime.now().year

# CREATE DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bookshelf.db"

# CREATE THE EXTENSION
db = SQLAlchemy()

# INITIALIZE THE APP WITH THE EXTENSION
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# Create table schema in the database, Require application context
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # Query all books from the database
    books = Book.query.all()
    return render_template('index.html', books=books, year=current_year)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]

        # Check if the rating is greater than 10
        if float(rating) > 10:
            return "Rating must be 10 or less"

        try:
            new_book = Book(title=title, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('home'))
        except IntegrityError as e:
            db.session.rollback()
            return "This book already exists in the database."

    return render_template("add.html", year=current_year)


@app.route("/edit_rating/<int:book_id>", methods=["GET", "POST"])
def edit_rating(book_id):
    book = Book.query.get(book_id)

    if not book:
        return "Book not found."

    if request.method == "POST":
        new_rating = float(request.form["rating"])
        if 0 <= new_rating <= 10:
            book.rating = new_rating
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return "Invalid rating. Please enter a value between 0 and 10."

    return render_template("edit_rating.html", book=book, year=current_year)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
