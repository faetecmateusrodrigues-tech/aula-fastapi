from sqlalchemy import Column, Integer, String, Float
from database import Base

class Curso(Base):
    __tablename__ = "cursos"

    id      = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome    = Column(String(100), nullable=False)
    descricao       = Column(String(200), nullable=True)
    carga_hor       = Column(Integer, nullable=False)
    preco       = Column(Float, default=0.0)

    def __repr__(self):
        return f"curso id={self.id} nome={self.nome}"