import os
from pathlib import Path
from dotenv import load_dotenv

# Encontra a pasta raiz do backend de forma dinâmica
BASE_DIR = Path(__file__).resolve().parent.parent

DOTENV_PATH = str(BASE_DIR / ".env")
load_dotenv(dotenv_path=DOTENV_PATH)

class Settings:
  def __init__(self):
    self.DATABASE_URL = os.getenv('DATABASE_URL')
    self.APP_NAME = os.getenv('APP_NAME')

    if not self.DATABASE_URL:
      raise ValueError(f"DATABASE_URL não encontrada em: {DOTENV_PATH}")

settings = Settings()