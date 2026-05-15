from sqlalchemy import String, Integer, Column, Boolean
from app.database import Base, engine, SessionLocal

class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(String)
    description = Column(String)
    page = Column(Integer, default=0)
    read = Column(Boolean, default=False)


# title = "Senhor dos betas"
# author = "Neymar"
# year = "antes de Cisto"
# description = (
#         """ Explora como alcançar paz interior em meio às dificuldades da vida. Discute equilíbrio emocional, propósito e a importância da moderação."""
#     )
# read = True
# page = 12
# novo = Books(
#         title=title,
#         author=author,
#         year=year,
#         description=description,
#         page=page,
#         read=read,
#     )
# db = SessionLocal()
# db.add(novo)
# db.commit()

Base.metadata.create_all(bind=engine)
