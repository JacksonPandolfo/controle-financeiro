from sqlalchemy.orm import Session
from backend.models.categoria import Categoria

def create(db: Session, data: dict):
  obj = Categoria(**data)

  db.add(obj)
  db.commit()
  db.refresh(obj)

  return obj

def get_all(db: Session):
  return db.query(Categoria).all()

def get_by_id(db: Session, categoria_id: str):
  #Busca pelo primeiro resultado que tenha o mesmo ID
  return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def get_by_nome(db: Session, nome: str):
  return db.query(Categoria).filter(Categoria.nome == nome).first()

def update(db: Session, obj: Categoria, data: dict):
  for key, value in data.items():
    setattr(obj, key, value) #Atualiza de forma dinâmica qualquer campo que tenha alterado 

  db.commit()
  db.refresh(obj)

  return obj

def delete(db: Session, obj: Categoria):
  db.delete(obj)
  db.commit()