from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.dependencies import get_current_user
from backend.core.exceptions import ConflictError, NotFoundError, UnauthorizedError
from backend.schemas.usuario_schema import (
  LoginSchema,
  UsuarioCreate, 
  UsuarioResponse, 
  UsuarioUpdate
)
from backend.services import usuario_service
from backend.db.session import get_db

router = APIRouter(prefix="/usuario", tags=["Usuarios"])

@router.post("/", response_model=UsuarioResponse)
def criar_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
  try:
    return usuario_service.create(db, data)
  except ConflictError as e:
    raise HTTPException(status_code=409, detail=str(e))
  
@router.post("/login")
def login_usuario(data: LoginSchema, db: Session = Depends(get_db)):
  try:
    return usuario_service.login(db, data.email, data.senha)
  except UnauthorizedError as e:
    raise HTTPException(status_code=401, detail=str(e))
  
@router.get("/{id}", response_model=UsuarioResponse, dependencies= [Depends(get_current_user)])
def buscar_usuario_por_id(id: str, db: Session = Depends(get_db)):
  try:
    return usuario_service.get_by_id(db, id)
  except NotFoundError as e:
    raise HTTPException(status_code=404, detail=str(e))
  
@router.put("/{id}", response_model=UsuarioResponse, dependencies= [Depends(get_current_user)])
def atualizar_usuario(data: UsuarioUpdate, id: str, usuario = Depends(get_current_user), db: Session = Depends(get_db)):
  try:
    return usuario_service.update(db, id, data, usuario.id)
  except NotFoundError as e:
    raise HTTPException(status_code=400, detail=str(e))
  except ConflictError as e:
    raise HTTPException(status_code=409, detail=str(e))
  except UnauthorizedError as e:
    raise HTTPException(status_code=401, detail=str(e))
  
@router.delete("/{id}", dependencies= [Depends(get_current_user)])
def deletar_usuario(id: str, usuario = Depends(get_current_user), db: Session = Depends(get_db)):
  try:
    usuario_service.delete(db, id, usuario.id)
    return {"message": "Usuário excluido com sucesso"}
  except NotFoundError as e:
    raise HTTPException(status_code=404, detail=str(e))
  except UnauthorizedError as e:
    raise HTTPException(status_code=401, detail=str(e))