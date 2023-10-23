# ---------------------------- SQLite 3 --------------------------------------------------- #
# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books "
# #                "(id INTEGER PRIMARY KEY, "
# #                "title varchar(250) NOT NULL UNIQUE, "
# #                "author varchar(250) NOT NULL, "
# #                "rating FLOAT NOT NULL)"
# #                )
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# ____________________________________________________________________________________________ #
# ---------------------------- SQL Alchemy --------------------------------------------------- #
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CREATE DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy()

# Initialise the app with the extension
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # This will allow each book object to be identified by its title when printed (optional)
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database, Require application context
with app.app_context():
    db.create_all()

# Create Record
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating="9.3")
    db.session.add(new_book)
    db.session.commit()

