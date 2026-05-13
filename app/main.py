from fastapi import Request, FastAPI, status
from app.routes.book_router import router
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Alpha Books")
templates = Jinja2Templates(directory="app/view/templates")

app.mount("/static", StaticFiles(directory="app/view/static"), name="static")
app.include_router(router)
# python -m uvicorn app.main:app --reload