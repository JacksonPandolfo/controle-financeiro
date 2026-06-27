from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session

from backend.db.session import get_db
from backend.repositories import usuario_repository


def get_current_user(
    usuario_id: str = Header(...),
    db: Session = Depends(get_db)
):
    if not usuario_id:
        raise HTTPException(status_code=401, detail="Usuário não autenticado")
    usuario = usuario_repository.get_by_id(db, usuario_id)

    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não autenticado")

    return usuario