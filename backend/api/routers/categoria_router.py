from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.dependencies import get_current_user
from backend.core.exceptions import ConflictError, NotFoundError
from backend.schemas.categoria_schema import (
  CategoriaCreate, 
  CategoriaResponse, 
  CategoriaUpdate
)
from backend.services import categoria_service
from backend.db.session import get_db

router = APIRouter(prefix="/categoria", tags=["Categorias"], dependencies= [Depends(get_current_user)])

@router.post("/", response_model=CategoriaResponse)
def criar_categoria(
  data: CategoriaCreate,
  db: Session = Depends(get_db)
):
  try:
    return categoria_service.create(db, data)
  except ConflictError as e:
    raise HTTPException(status_code=409, detail=str(e))

@router.get("/", response_model=list[CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return categoria_service.get_all(db)

@router.get("/{categoria_id}", response_model=CategoriaResponse)
def buscar_categoria_por_id(categoria_id: str, db: Session = Depends(get_db)):
  try:
    return categoria_service.get_by_id(db, categoria_id)
  except NotFoundError as e:
    raise HTTPException(status_code=404, detail=str(e))

@router.put("/{categoria_id}", response_model=CategoriaResponse)
def atualizar_categoria(
  categoria_id: str, 
  data: CategoriaUpdate, 
  db: Session = Depends(get_db)
):
  try:
    return categoria_service.update(db, categoria_id, data)
  except NotFoundError as e:
    raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{categoria_id}")
def deletar_categoria(categoria_id: str, db: Session = Depends(get_db)):
  try:
    categoria_service.delete(db, categoria_id)
    return {"message": "Categoria excluida com sucesso"}
  except NotFoundError as e:
    raise HTTPException(status_code=404, detail=str(e))