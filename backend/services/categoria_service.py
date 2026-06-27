from sqlalchemy.orm import Session
from fastapi import HTTPException

from backend.core.exceptions import ConflictError, NotFoundError
from backend.repositories import categoria_repository
from backend.schemas.categoria_schema import CategoriaCreate, CategoriaResponse, CategoriaUpdate

def create(db: Session, data: CategoriaCreate):
  #Verifica se a categoria existe
  categoria = categoria_repository.get_by_nome(db, data.nome)

  if categoria:
    raise ConflictError("Categoria já está cadastrada")
  
  #Cria o objeto com o usuario
  nova_categoria = {
    **data.model_dump(),
  }

  return categoria_repository.create(db, nova_categoria)

def get_all(db: Session):
  return categoria_repository.get_all(db)

def get_by_id(db: Session, categoria_id: str):
  categoria = categoria_repository.get_by_id(db, categoria_id)

  if not categoria:
    raise NotFoundError("Categoria não encontrada")
  
  return categoria

def update(db: Session, categoria_id: str, data: CategoriaUpdate):
  categoria = categoria_repository.get_by_id(db, categoria_id)

  if not categoria:
    raise NotFoundError("Categoria não encontrada")
  
  update_data = data.model_dump(exclude_unset=True)

  return categoria_repository.update(db, categoria, update_data)

def delete(db: Session, categoria_id: str):
  categoria = categoria_repository.get_by_id(db, categoria_id)

  if not categoria:
    raise NotFoundError("Categoria não encontrada")
  
  categoria_repository.delete(db, categoria)