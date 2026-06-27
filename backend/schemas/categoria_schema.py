from pydantic import BaseModel

class CategoriaBase(BaseModel):
  nome: str

class CategoriaCreate(CategoriaBase):
  pass

class CategoriaResponse(CategoriaBase):
  id: str

  class Config:
    from_attributes = True

class CategoriaUpdate(BaseModel):
  nome: str | None = None