from datetime import datetime
import uuid
from sqlalchemy import UUID, Column, DateTime, Float, ForeignKey, String, Enum as SQLEnum
from sqlalchemy.orm import relationship
from backend.core.enums import TipoTransacao
from backend.db.base import Base

class Transacao(Base):
  __tablename__ = "transacoes"

  id = Column(String, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
  valor = Column(Float, nullable=False)
  tipo = Column(SQLEnum(TipoTransacao), nullable=False) #Entrada ou saída
  descricao = Column(String)

  data_hora = Column(DateTime, default=datetime.now)

  #Relacionamentos
  usuario_id = Column(String, ForeignKey("usuarios.id"))
  categoria_id = Column(String, ForeignKey("categorias.id"))

  #Relationship deve receber o nome da classe
  usuario = relationship("Usuario", back_populates="transactions") 
  categoria = relationship("Categoria", back_populates="transactions")