from models.usuario import Usuario

class ServicoFinanceiro:
    @staticmethod
    def calcular_saldo(usuario: Usuario):
        transacoes = usuario.listar_transacoes()
        saldo = 0
        for t in transacoes:
            if t.tipo == "receita":
                saldo += t.valor
            else:
                saldo -= t.valor
        return saldo
