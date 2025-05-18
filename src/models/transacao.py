from datetime import datetime

from models.categoria import CategoriaReceita, CategoriaDespesa

class Transacao:
    id: int
    valor: float
    tipo: str
    categoria: CategoriaReceita | CategoriaDespesa
    data: datetime

    def __init__(self, id: int, valor: float, tipo: str, categoria: CategoriaReceita | CategoriaDespesa, data: datetime):
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.categoria = categoria
        self.data = data

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "tipo": self.tipo,
            "valor": self.valor,
            "categoria": self.categoria.value,
            "data": self.data.isoformat()
        }