from sqlalchemy import desc
from sqlalchemy.orm import Session, joinedload
from backend.models.transacao import Transacao

def create(db: Session, data: dict):
  obj = Transacao(**data)

  db.add(obj)
  db.commit()
  db.refresh(obj)

  return obj

def get_all(db: Session, usuario_id: str):
  return (
    db.query(Transacao)
    .filter(Transacao.usuario_id == usuario_id)
    .options(joinedload(Transacao.categoria))
    .order_by(desc(Transacao.data_hora))
    .all()
  )

def get_by_id(db: Session, transacao_id: str):
  #Busca pelo primeiro resultado que tenha o mesmo ID
  return (
    db.query(Transacao)
    .filter(Transacao.id == transacao_id)
    .options(joinedload(Transacao.categoria))
    .first()
  )

def update(db: Session, obj: Transacao, data: dict):
  for key, value in data.items():
    setattr(obj, key, value) #Atualiza de forma dinâmica qualquer campo que tenha alterado 

  db.commit()
  db.refresh(obj)

  return obj

def delete(db: Session, obj: Transacao):
  db.delete(obj)
  db.commit()