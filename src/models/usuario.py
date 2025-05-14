from models.transacao import Transacao
from models.categoria import Categoria
from datetime import date

class Usuario:
    id: int
    nome: str
    transacoes: list[Transacao]

    def __init__(self, id: int, nome: str) -> None:
        self.id = id
        self.nome = nome
        self.transacoes = []

    def adicionar_transacao(self, t: Transacao) -> None:
        self.transacoes.append(t)

    def listar_transacoes(self) -> list[Transacao]:
        return self.transacoes

    def listar_por_categoria(self, c: Categoria) -> list[Transacao]:
        resultado = []
        for t in self.transacoes:
            if t.categoria == c:
                resultado.append(t)
        return resultado

    def listar_por_data(self, data: date) -> list[Transacao]:
        resultado = []
        for t in self.transacoes:
            if t.data.date() == data.date():
                resultado.append(t)
        return resultado
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "transacoes": [t.to_dict() for t in self.transacoes]
        }