from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
  nome: str
  email: EmailStr

class UsuarioCreate(UsuarioBase):
  senha: str

class LoginSchema(BaseModel):
  email: EmailStr
  senha: str

class UsuarioResponse(UsuarioBase):
  id: str

  class Config:
    from_attributes = True

class UsuarioUpdate(BaseModel):
  nome: str | None = None
  email: EmailStr | None = None
  senha: str | None = None
