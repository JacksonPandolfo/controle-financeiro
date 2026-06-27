from sqlalchemy.orm import Session
from backend.core.exceptions import UnauthorizedError
from backend.models.usario import Usuario

def create(db: Session, data: dict):
  obj = Usuario(**data)
  db.add(obj)
  db.commit()
  db.refresh(obj)

  return obj

def get_by_id(db: Session, usuario_id: str):
  #Busca pelo primeiro resultado que tenha o mesmo ID
  return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def get_by_email(db: Session, email: str):
  #Busca pelo primeiro resultado que tenha o mesmo email
  return db.query(Usuario).filter(Usuario.email == email).first()

def update(db: Session, obj: Usuario, data: dict):
  for key, value in data.items():
    setattr(obj, key, value) #Atualiza de forma dinâmica qualquer campo que tenha alterado 

  db.commit()
  db.refresh(obj)

  return obj

def delete(db: Session, obj: Usuario):
  db.delete(obj)
  db.commit()