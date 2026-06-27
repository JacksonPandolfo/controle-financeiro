import uuid

from sqlalchemy import UUID, Column, String
from sqlalchemy.orm import relationship
from backend.db.base import Base

class Usuario(Base):
  __tablename__ = "usuarios"

  id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))

  nome = Column(String, nullable=False)
  email = Column(String, unique=True, nullable=False, index=True)
  senha = Column(String, nullable=False)

  #Relacionamento
  #Relationship deve receber o nome da classe
  transactions = relationship("Transacao", back_populates="usuario")