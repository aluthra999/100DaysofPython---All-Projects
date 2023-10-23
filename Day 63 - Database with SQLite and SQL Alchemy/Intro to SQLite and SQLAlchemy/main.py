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
    # def __repr__(self):
    #     return f'<Book {self.title}>'


# Create table schema in the database, Require application context
with app.app_context():
    db.create_all()

# CRUD (Create, Read, Update, Delete) Operations
# Create Record
with app.app_context():
    # id is optional, database will create an id automatically
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating="9.3")
    db.session.add(new_book)
    db.session.commit()

# Read all Records
# To read all the records we first need to create a "query" to select things from the database.
# When we execute a query during a database session we get back the rows in the database (a Result object).
# We then use scalars() to get the individual elements rather than entire rows.
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()


# Read A Particular Record By Query
# To get a single element we can use 'scalar()' instead of 'scalars()'
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

# Update A Particular Record By Query
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

# Update A Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

# Delete A Particular Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

