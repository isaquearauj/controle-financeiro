from pathlib import Path
from datetime import date, datetime
from typing import Type
from enum import Enum

from models.usuario import Usuario
from models.categoria import CategoriaReceita, CategoriaDespesa
from models.transacao import Transacao
from persistence.persistencia import Persistencia
from services.servico_financeiro import ServicoFinanceiro
from utils.decoradores import Decoradores

def menu_principal():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("[1] Novo usuário")
        print("[2] Usuário existente")
        print("[0] Sair")

        escolha: str = input("Escolha uma opção: ")
        if (escolha == '1'):
            cadastrar_usuario()
        elif (escolha == '2'):
            usuario = selecionar_usuario_existente()
            if usuario:
                menu_usuario(usuario)
            else:
                print("Falha no login. Verifique o username digitado.")
        elif (escolha == '0'):
            break
        else:
            print("Opção inválida!")

def menu_usuario(usuario: Usuario):
    while True:
        print(f"\n--- Usuário: {usuario.username} ---")
        print("[1] Consultar saldo")
        print("[2] Realizar transação")
        print("[3] Listar transações")
        print("[4] Exportar transações em CSV")
        print("[0] Sair")

        escolha: str = input("Escolha uma opção: ")

        if escolha == '1':
            mostrar_saldo(usuario)
        elif escolha == '2':
            registrar_transacao(usuario)
        elif escolha == '3':
            verificar_transacoes(usuario)
        elif escolha == '4':
            Persistencia.exportar_csv(usuario)
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")     

@Decoradores.log_acao("Usuário cadastrado")
def cadastrar_usuario():
    while True:
        username: str = input("Digite seu nome de usuário: ")
        if usuario_ja_existe(username):
            print("\nEsse username já existe!")
        else:
            novo: Usuario = Usuario(id=0, username=username)
            Persistencia.salvar(novo)
            print(f"\nBoas vindas {novo.username}!")
            menu_usuario(novo)
            break

def usuario_ja_existe(username) -> bool:
    path: Path = Path(__file__).resolve().parents[1] / "data"

    if not path.exists():
        return False

    for arquivo in path.iterdir():
        if arquivo.is_file() and arquivo.suffix == ".json":
            partes: list[str] = arquivo.stem.split("_")
            if len(partes) >= 2:
                nome: str = partes[0]
                if nome.lower() == username.lower():
                    return True
    return False

@Decoradores.log_acao("Login efetuado")
def selecionar_usuario_existente():
    username: str = input("Digite seu username: ")
    username = username.lower().replace(" ", "_")
    return Persistencia.carregar(username)

@Decoradores.log_usuario("Saldo consultado")
def mostrar_saldo(usuario: Usuario) -> None:
    saldo: float = ServicoFinanceiro.calcular_saldo(usuario)
    print(f"\nSaldo atual: R$ {saldo:.2f}")

@Decoradores.log_usuario("Transação registrada")
def registrar_transacao(usuario: Usuario):
    tipo_str = None
    while tipo_str is None:
        tipo: str = input("\nTipo de transação ([1] Receita, [2] Despesa): ")
        if tipo == '1':
            tipo_str = "receita"
        elif tipo == '2':
            tipo_str = "despesa"
        else:
            print("Tipo inválido.")
            tipo_str = None
    
    valor: float = 0
    while (valor <= 0):
        try:
            valor = float(input("Digite o valor: "))
            if valor <= 0:
                print("Valor inválido.")
        except ValueError:
            print("Digite um número válido.")
    
    if tipo_str == "despesa":
        saldo = ServicoFinanceiro.calcular_saldo(usuario)
        if valor > saldo:
            print(f"Saldo insuficiente. Saldo atual: R$ {saldo:.2f}")
            return None

    categoria: CategoriaReceita | CategoriaDespesa | None = None
    while categoria is None:
        if tipo_str == "receita":
            categoria = selecionar_categoria_por_numero(CategoriaReceita)
        else:
            categoria = selecionar_categoria_por_numero(CategoriaDespesa)


    data = datetime.now()
    novo_id = len(usuario.transacoes) + 1
    transacao = Transacao(id=novo_id, valor=valor, tipo=tipo_str, categoria=categoria, data=data)
    usuario.adicionar_transacao(transacao)
    Persistencia.salvar(usuario)

@Decoradores.log_usuario("Listagem de transações")
def verificar_transacoes(usuario: Usuario):
    while True:
        print("\n--- EXTRATO ---")
        print("[1] Todas as transações")
        print("[2] Por categoria")
        print("[3] Por data")
        print("[0] Voltar")

        opcao: str = input("Digite a opção desejada: ")

        if opcao == '1':
            transacoes: list[Transacao] = usuario.listar_transacoes()
            exibir_transacoes(transacoes)

        elif opcao == '2':
            tipo_categoria = input("Deseja filtrar por [1] Receita ou [2] Despesa? ")
            categoria = None

            if tipo_categoria == '1':
                while categoria is None:
                    categoria = selecionar_categoria_por_numero(CategoriaReceita)
            elif tipo_categoria == '2':
                while categoria is None:
                    categoria = selecionar_categoria_por_numero(CategoriaDespesa)
            else:
                print("Tipo inválido.")
                continue

            transacoes: list[Transacao] = usuario.listar_por_categoria(categoria)
            exibir_transacoes(transacoes)

        elif opcao == '3':
            data_str: str = input("Digite a data no formato DD-MM-AAAA: ")
            try:
                data: date = datetime.strptime(data_str, "%d/%m/%Y").date()
                transacoes: list[Transacao] = usuario.listar_por_data(data)
                exibir_transacoes(transacoes)
            except ValueError:
                print("Data inválida. Use o formato correto.")

        elif opcao == '0':
            break
        else:
            print("Opção inválida")

def selecionar_categoria_por_numero(enum_categoria: CategoriaReceita.__class__ | CategoriaDespesa.__class__) -> CategoriaReceita | CategoriaDespesa | None:
    categorias = list(enum_categoria)
    print("Categorias disponíveis:")
    for i, c in enumerate(categorias, start=1): 
        print(f"[{i}] {c.value}")

    try:
        escolha = int(input("Escolha a categoria pelo número: "))
        if 1 <= escolha <= len(categorias):
            return categorias[escolha - 1]
        else:
            print("Opção inválida.")
    except ValueError:
        print("Digite um número válido.")

    return None

def exibir_transacoes(transacoes: list[Transacao]) -> None:
    print()

    if not transacoes:
        print("Nenhuma transação encontrada.")
        return
    
    for t in transacoes:
        print(f"[{t.data.strftime('%d/%m/%Y %H:%M')}] "
                f"{t.tipo.upper()} - R${t.valor:.2f} - {t.categoria.value}")

menu_principal()