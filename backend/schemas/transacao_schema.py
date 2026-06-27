from datetime import datetime

from pydantic import BaseModel, Field
from sqlalchemy import DateTime

from backend.core.enums import TipoTransacao
from backend.schemas.categoria_schema import CategoriaResponse
from backend.schemas.usuario_schema import UsuarioResponse

class TransacaoBase(BaseModel):
  valor: float = Field(gt=0)
  tipo: TipoTransacao
  descricao: str | None = None
  categoria_id: str

class TransacaoCreate(TransacaoBase):
  valor: float = Field(gt=0)
  tipo: TipoTransacao
  descricao: str | None = None
  categoria_id: str

class TransacaoResponse(TransacaoBase):
  id: str
  categoria: CategoriaResponse
  usuario: UsuarioResponse
  data_hora: datetime

  class Config:
    from_attributes = True

class TransacaoUpdate(BaseModel):
  valor: float | None = Field(default=None, gt=0)
  tipo: TipoTransacao | None = None
  descricao: str | None = None
  categoria_id: str | None = None
  usuario_id: str | None = None

