from sqlalchemy import String, Integer, Column, Boolean
from database import Base, engine, SessionLocal

class Books(Base):
    __tablename__= "books"
    id= Column(Integer, primary_key=True, index=True)
    title= Column(String, nullable=False)
    author= Column(String, nullable=False)
    year= Column(String)
    description= Column(String)
    read= Column(Boolean, default=False)


title="Sobre a Tranquilidade da Alma"
author= "Sêneca"
year="~60 d.C."
description= """ Explora como alcançar paz interior em meio às dificuldades da vida. Discute equilíbrio emocional, propósito e a importância da moderação."""
read= False
novo=Books(title=title,author=author,year=year,
             description=description, read=read)
db=SessionLocal() 
db.add(novo)
db.commit()

Base.metadata.create_all(bind=engine)