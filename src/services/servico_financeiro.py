from models.usuario import Usuario
from models.transacao import Transacao

class ServicoFinanceiro:
    @staticmethod
    def calcular_saldo(usuario: Usuario):
        transacoes: list[Transacao] = usuario.listar_transacoes()
        saldo: float = 0
        for t in transacoes:
            if t.tipo == "receita":
                saldo += t.valor
            else:
                saldo -= t.valor
        return saldo