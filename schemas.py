from pydantic import BaseModel, Field
from typing import Optional

class CursoBase(BaseModel):
    nome:           str = Field(..., min_length=3, max_length=100)
    descricao:      Optional[str] = Field(None, max_length=300)
    carga_hor:      int = Field(..., gt=0)
    preco:         float = Field(0.0, ge=0.0)

class CursoCreate(CursoBase):
    pass

class CursoUpdate(CursoBase):
    nome: Optional[str] =       None
    descricao: Optional[str] =      None
    carga_hor: Optional[int] =       None
    preco: Optional[float] =        None
    

class CursoResponse(CursoBase):
    id: int

    class Config:
        from_attributes = True 