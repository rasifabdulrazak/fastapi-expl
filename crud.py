from sqlalchemy.orm import Session
from model import Book
from schema import BookSchema


def get_book(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, book: BookSchema):
    print("]]]]]]]]]]")
    _book = Book(title=book.title, description=book.description)
    print(_book,"=======")
    db.add(_book)
    print("-=-==---=")
    db.commit()
    db.refresh(_book)
    return {"ok":'created'}


def remove_book(db: Session, book_id: int):
    _book = get_book_by_id(db=db, book_id=book_id)
    db.delete(_book)
    db.commit()


def update_book(db: Session, book_id: int, title: str, description: str):
    _book = get_book_by_id(db=db, book_id=book_id)

    _book.title = title
    _book.description = description

    db.commit()
    db.refresh(_book)
    return _book


dictoi = {'a':1,'b':2,'c':1,'d':2,'e':3}
result = {1:['a','c'],2:['b','d'],3:['e']}