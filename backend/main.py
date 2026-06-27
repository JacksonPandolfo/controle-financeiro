from fastapi import FastAPI
from fastapi import FastAPI
from backend.api.routers import categoria_router, transacao_router, usuario_router
from backend.db.base import Base
from backend.db.session import engine
from backend import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(transacao_router.router)
app.include_router(usuario_router.router)
app.include_router(categoria_router.router)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)