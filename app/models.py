from sqlalchemy import String, Integer, Column, Boolean
from database import Base, engine, SessionLocal

class Books(Base):
    __tablename__= "books"
    id= Column(Integer, primary_key=True, index=True)
    title= Column(String, nullable=False)
    author= Column(String, nullable=False)
    year= Column(Integer)
    description= Column(String)
    read= Column(Boolean, default=False)


title="A Psicologia Finaceira"
author= "Morgan Housel"
year=2020
description= """ O livro aborda como o comportamento, 
    emoções e experiências pessoais influenciam as decisões financeiras, 
    mais do que o conhecimento técnico."""
read= False
novo=Books(title=title,author=author,year=year,
             description=description, read=read)
db=SessionLocal() 
db.add(novo)
db.commit()

Base.metadata.create_all(bind=engine)