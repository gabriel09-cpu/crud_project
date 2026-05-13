from app.database import get_db
from app.models import Books
from fastapi import APIRouter, Request, Form, UploadFile, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os


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
    books = db.query(Books).filter(Books.id == id_books).first()
    
    outros_livros = db.query(Books).filter(Books.id != id_books).all()
    
    return templates.TemplateResponse("details.html", {
        "request":request, "books":books
    })