from app.database import get_db
from app.models import Books
from fastapi import APIRouter, Request, Form, UploadFile, Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

import os
import sqlite3 as sq


app= FastAPI()
router = APIRouter()
templates = Jinja2Templates(directory="app/view/templates")

UPLOAD_DIR = "app/view/static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

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

@router.get("/books/{id_books}", response_class=HTMLResponse )
async def details_id(request:Request, id_books:int, db:Session=Depends(get_db)):
    book = db.query(Books).filter(Books.id == id_books).first()
    
    outros_livros = db.query(Books).filter(Books.id != id_books).all()
    
    return templates.TemplateResponse("details.html", {
        "request":request, "book":book
    })

@router.delete("/books/delete")
async def delete_books(request:Request, id_book:int, db:Session=Depends(get_db)):
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