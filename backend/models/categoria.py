import uuid

from sqlalchemy import UUID, Column, String
from backend.db.base import Base
from sqlalchemy.orm import relationship

class Categoria(Base):
  __tablename__ = "categorias"

  id = Column(String, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
  nome = Column(String, unique=True, nullable=False)

  #Relacionamento
  #Relationship deve receber o nome da classe
  transactions = relationship("Transacao", back_populates="categoria")