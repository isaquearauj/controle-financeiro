from enum import Enum

class CategoriaReceita(Enum):
    SALARIO = "SALÁRIO"
    OUTROS = "OUTROS"

    @classmethod
    def listar_categorias(cls) -> list[str]:
        return [categoria.value for categoria in cls]

class CategoriaDespesa(Enum):
    ALIMENTACAO = "ALIMENTAÇÃO"
    TRANSPORTE = "TRANSPORTE"
    LAZER = "LAZER"
    OUTROS = "OUTROS"

    @classmethod
    def listar_categorias(cls) -> list[str]:
        return [categoria.value for categoria in cls]
