from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.dependencies import get_current_user
from backend.core.exceptions import NotFoundError, UnauthorizedError
from backend.schemas.transacao_schema import (
    TransacaoCreate,
    TransacaoResponse,
    TransacaoUpdate
)
from backend.services import transacao_service
from backend.db.session import get_db

router = APIRouter(prefix="/transacoes", tags=["Transações"], dependencies= [Depends(get_current_user)])

@router.post("/", response_model=TransacaoResponse)
def criar_transacao(
  data: TransacaoCreate,
  usuario = Depends(get_current_user),
  db: Session = Depends(get_db)
):
  try:
    return transacao_service.create(db, data, usuario.id)
  except NotFoundError as e:
    raise HTTPException(status_code=404, detail=str(e))
  
@router.get("/", response_model=list[TransacaoResponse])
def listar_transacoes(usuario = Depends(get_current_user), db: Session = Depends(get_db)):
  return transacao_service.get_all(db, usuario.id)


@router.get("/{transacao_id}", response_model=TransacaoResponse)
def buscar_transacao_por_id(transacao_id: str, usuario = Depends(get_current_user), db: Session = Depends(get_db)):
  try:
    return transacao_service.get_by_id(db, transacao_id, usuario.id)
  except NotFoundError as e:
    raise HTTPException(status_code=404, detail=str(e))
  except UnauthorizedError as e:
    raise HTTPException(status_code=401, detail=str(e))

@router.put("/{transacao_id}", response_model=TransacaoResponse)
def atualizar_transacao(
  transacao_id: str, 
  data: TransacaoUpdate,
  usuario = Depends(get_current_user), 
  db: Session = Depends(get_db)
):
  try:
    return transacao_service.update(db, transacao_id, data, usuario.id)
  except NotFoundError as e:
    raise HTTPException(status_code=404, detail=str(e))
  except UnauthorizedError as e:
    raise HTTPException(status_code=401, detail=str(e))

@router.delete("/{transacao_id}")
def deletar_transacao(transacao_id: str, usuario = Depends(get_current_user), db: Session = Depends(get_db)):
  try:
    transacao_service.delete(db, transacao_id, usuario.id)
  except NotFoundError as e:
    raise HTTPException(status_code=404, detail=str(e))
  except UnauthorizedError as e:
    raise HTTPException(status_code=401, detail=str(e))

  return {"message": "Transação excluida com sucesso"}