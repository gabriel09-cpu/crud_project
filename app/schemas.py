from pydantic import BaseModel
from typing import Optional

# Pydantic schemas para validação/serialização de dados relacionados a `Book`.
# Use estes modelos nas rotas para garantir entrada/saída consistente.


# Schema base com os campos compartilhados entre criação, atualização e resposta.
class BookBase(BaseModel):
    # `title`: título do livro (obrigatório)
    title: str
    # `author`: nome do autor (obrigatório)
    author: str
    # `year`: ano de publicação ou edição (opcional, string para permitir formatos variados)
    year: Optional[str] = None
    # `description`: sinopse ou observações sobre o livro (opcional)
    description: Optional[str] = None
    # `page`: número de páginas lidas/total (opcional, padrão 0)
    page: Optional[int] = 0
    # `read`: indica se o livro já foi lido (opcional, padrão False)
    read: Optional[bool] = False


# Schema usado ao criar um novo livro (herda todos os campos obrigatórios de BookBase).
class BookCreate(BookBase):
    pass


# Schema para atualizações parciais: todos os campos são opcionais.
# Use este modelo em endpoints PATCH/PUT que aceitam campos parciais.
class BookUpdate(BaseModel):
    # Cada campo é opcional para permitir atualizações parciais.
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[str] = None
    description: Optional[str] = None
    page: Optional[int] = None
    read: Optional[bool] = None


# Schema de resposta que inclui o `id` do objeto persistido.
class Book(BookBase):
    # `id`: identificador gerado pelo banco (inteiro)
    id: int

    class Config:
        # Permite a compatibilidade com objetos ORM (SQLAlchemy) ao retornar modelos
        orm_mode = True