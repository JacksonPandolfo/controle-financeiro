from enum import Enum

class TipoTransacao(str, Enum):
    ENTRADA = "entrada"
    SAIDA = "saida"