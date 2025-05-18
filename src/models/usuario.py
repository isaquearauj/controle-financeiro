from datetime import date

from models.transacao import Transacao
from models.categoria import CategoriaReceita, CategoriaDespesa

class Usuario:
    id: int
    username: str
    transacoes: list[Transacao]

    def __init__(self, id: int, username: str) -> None:
        self.id = id
        self.username = username
        self.transacoes = []

    def adicionar_transacao(self, t: Transacao) -> None:
        self.transacoes.append(t)

    def listar_transacoes(self) -> list[Transacao]:
        return self.transacoes

    def listar_por_categoria(self, c: CategoriaReceita | CategoriaDespesa) -> list[Transacao]:
        resultado: list[Transacao] = []
        for t in self.transacoes:
            if t.categoria == c:
                resultado.append(t)
        return resultado

    def listar_por_data(self, data: date) -> list[Transacao]:
        resultado: list[Transacao] = []
        for t in self.transacoes:
            if t.data.date() == data:
                resultado.append(t)
        return resultado
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "transacoes": [t.to_dict() for t in self.transacoes]
        }