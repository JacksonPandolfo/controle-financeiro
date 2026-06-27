from sqlalchemy.orm import Session
from fastapi import HTTPException

from backend.core.exceptions import NotFoundError, UnauthorizedError
from backend.repositories import transacao_repository
from backend.repositories import categoria_repository
from backend.schemas.transacao_schema import TransacaoCreate, TransacaoUpdate

def create(db: Session, data: TransacaoCreate, usuario_id: str):
  #Verifica se a categoria existe
  categoria = categoria_repository.get_by_id(db, data.categoria_id)

  if not categoria:
    raise NotFoundError("Categoria não encontrada")

  return transacao_repository.create(db, {**data.model_dump(), "usuario_id": usuario_id})

def get_all(db: Session, usuario_id: str):
  return transacao_repository.get_all(db, usuario_id)

def get_by_id(db: Session, transacao_id: str, usuario_id: str):
  transacao = transacao_repository.get_by_id(db, transacao_id)
  if transacao.usuario_id != usuario_id:
    raise UnauthorizedError("Você não tem permissão para visualizar essa transação")
  if not transacao:
    raise NotFoundError("Transação não encontrada")
  
  return transacao

def update(db: Session, transacao_id: str, data: TransacaoUpdate, usuario_id: str):
  transacao = transacao_repository.get_by_id(db, transacao_id)

  if not transacao:
    raise NotFoundError("Transação não encontrada")

  if transacao.usuario_id != usuario_id:
    raise UnauthorizedError("Você não tem permissão para alterar essa transação")

  
  #Valida categoria se for enviada
  if data.categoria_id:
    categoria = categoria_repository.get_by_id(db, data.categoria_id)

    if not categoria:
      raise NotFoundError("Categoria não encontrada")
  
  update_data = data.model_dump(exclude_unset=True)

  return transacao_repository.update(db, transacao, update_data)

def delete(db: Session, transacao_id: str, usuario_id: str):
  transacao = transacao_repository.get_by_id(db, transacao_id)

  if transacao.usuario_id != usuario_id:
    raise UnauthorizedError("Você não tem permissão para excluir essa transação")

  if not transacao:
    raise NotFoundError("Transação não encontrada")
  
  transacao_repository.delete(db, transacao)