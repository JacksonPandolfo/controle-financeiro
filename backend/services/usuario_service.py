from fastapi import HTTPException

from backend.core.exceptions import ConflictError, NotFoundError, UnauthorizedError
from backend.models.usario import Usuario
from backend.repositories import usuario_repository
from backend.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate
from sqlalchemy.orm import Session

def create(db: Session, data: UsuarioCreate):
  email = usuario_repository.get_by_email(db, data.email)

  if email:
    raise ConflictError("Email já cadastrado")
  
  novo_usuario = {
    **data.model_dump(),
  }

  return usuario_repository.create(db, novo_usuario)

def login(db: Session, email: str, senha: str):
  usuario = usuario_repository.get_by_email(db, email)

  if not usuario or usuario.senha != senha:
    raise UnauthorizedError("Email ou senha inválidos")
  
  return {
    "id": usuario.id,
    "nome": usuario.nome,
  }

def get_by_id(db: Session, usuario_id: str):
  usuario = usuario_repository.get_by_id(db, usuario_id)

  if not usuario:
    raise NotFoundError("Usuário não encontrado")
  
  return usuario

def update(db: Session, usuario_id: str, data: UsuarioUpdate, usuario_id_auth: str):
  usuario = usuario_repository.get_by_id(db, usuario_id)

  if not usuario:
    raise NotFoundError("Usuário não encontrado")
  
  if usuario.id != usuario_id_auth:
    raise UnauthorizedError("Você não tem permissão para alterar esse usuário")
  
  if data.email:
    email_usuario = usuario_repository.get_by_email(db, data.email)

    if email_usuario and usuario.id != email_usuario.id:
        raise ConflictError("Email já utilizado por outro usuário")
  
  update_data = data.model_dump(exclude_unset=True)
  return usuario_repository.update(db, usuario, update_data)

def delete(db: Session, usuario_id: str, usuario_id_auth: str):
  usuario = usuario_repository.get_by_id(db, usuario_id)
  
  if usuario.id != usuario_id_auth:
    raise UnauthorizedError("Você não tem permissão para deletar esse usuário")
  
  if not usuario:
    raise NotFoundError("Usuário não encontrado")
  
  return usuario_repository.delete(db, usuario)