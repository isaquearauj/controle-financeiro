from datetime import datetime

from models.categoria import  Categoria

class Transacao:
    id: int
    valor: float
    tipo: str
    categoria: Categoria
    data: datetime

    def __init__(self, id: int, valor: float, tipo: str, categoria: Categoria, data: datetime):
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.categoria = categoria
        self.data = data

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "valor": self.valor,
            "tipo": self.tipo,
            "categoria": self.categoria.value,
            "data": self.data.isoformat()
        }