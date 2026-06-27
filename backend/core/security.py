#Aqui posso colocar as funções de Hash, Auth, Tokens
from passlib.context import CryptContext

contexto_senha = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str):
    return contexto_senha.hash(senha)

def verificar_senha(senha: str, hash: str):
    return contexto_senha.verify(senha, hash)