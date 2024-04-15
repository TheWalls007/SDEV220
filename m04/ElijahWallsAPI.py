"""
API tutorial

Elijah Walls

API created using video tutorial

4/14/24
"""

from flask import Flask, request
from flask_squlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Interger, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = Flase)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'name': book.name, 'description': book.description}

        ouput.append(book_data)
        
    return{"drinks": "drink data"}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"name": book.name, "desription": book.description}

@app.route('/books', methods = ['POST'])
def add_books():
    book = Book(name=request.json['name'], description = request.json['description'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return{"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "yeet!@"}
