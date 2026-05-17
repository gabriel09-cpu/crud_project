from app.database import get_db
from app.models import Books
from app.schemas import Book, BookUpdate, BookCreate
from fastapi import APIRouter, Request, Depends, FastAPI, HTTPException, status, Form
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import os



app= FastAPI()
router = APIRouter()
templates = Jinja2Templates(directory="app/view/templates")

UPLOAD_DIR = "app/view/static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/books/create")
async def add_book(book_data: BookCreate, db: Session = Depends(get_db)):
    new_book = Books(**book_data.model_dump())

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.get("/", response_class=HTMLResponse)
async def page_books(request: Request, db:Session=Depends(get_db)):
    books = db.query(Books).all()
    return templates.TemplateResponse("home.html", {
        "request":request,
        "books":books
    })
@router.get("/books", response_class=HTMLResponse)
async def list_books(request:Request,
                     db:Session=Depends(get_db)):
    books = db.query(Books).all()
    return templates.TemplateResponse("home.html",{"request":request, "books":books})

@router.get("/books/{id_books}", response_class=HTMLResponse)
async def details_id(request: Request, id_books: int, db: Session = Depends(get_db)):
    book = db.query(Books).filter(Books.id == id_books).first()
    if not book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    outros_livros = db.query(Books).filter(Books.id != id_books).all()
    return templates.TemplateResponse("details.html", {
        "request": request,
        "book": book,
    })


@router.get("/api/books/{id_books}", response_model=Book)
async def get_book_json(id_books: int, db: Session = Depends(get_db)):
    book = db.query(Books).filter(Books.id == id_books).first()
    if not book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return book


@router.put("/api/books/{id_books}", response_model=Book)
async def update_book(id_books: int, book_data: BookUpdate, db: Session = Depends(get_db)):
    book_query = db.query(Books).filter(Books.id == id_books).first()
    if not book_query:
        raise HTTPException(status_code=404, detail=f"Livro com ID {id_books} não encontrado!")

    update_data = book_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(book_query, key, value)

    db.commit()
    db.refresh(book_query)
    return book_query


@router.delete("/books/delete")
async def delete_books(request: Request, id_book: int, db: Session = Depends(get_db)):
    book = db.query(Books).filter(Books.id == id_book).first()
    
    if not book:
        raise HTTPException(
            status_code=404,
            detail=f"Produto {id_book} não encontrado!"
        )
    db.delete(book)
    db.commit()

    return None

@router.delete("/books/range/{id_start}/{id_end}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_books_range(id_start: int, id_end: int, db: Session = Depends(get_db)):
    # 1. Filtra todos os livros onde o ID está entre id_start e id_end (inclusive)
    query = db.query(Books).filter(Books.id >= id_start, Books.id <= id_end)
    
    # 2. Executa a deleção
    # O synchronize_session=False é mais performático para deleções em lote
    query.delete(synchronize_session=False)
    
    # 3. Confirma a transação no banco
    db.commit()
    
    return None