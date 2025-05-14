from pathlib import Path

from models.usuario import Usuario
from persistence.persistencia_json import PersistenciaJson
from services.servico_financeiro import ServicoFinanceiro

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
        print("[0] Sair")

        escolha: str = input("Escolha uma opção: ")
        if escolha == '1':
            mostrar_saldo(usuario)
        elif escolha == '2':
            registrar_transacao(usuario)
        elif escolha == '3':
            verificar_transacoes(usuario)
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")     

def cadastrar_usuario():
    while True:
        username: str = input("Digite seu nome de usuário: ")
        if usuario_ja_existe(username):
            print("\nEsse username já existe!")
        else:
            novo: Usuario = Usuario(id=0, username=username)
            PersistenciaJson.salvar(novo)
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

def selecionar_usuario_existente():
    # TODO: implementar carregar() -> persistencia_json.py
    # TODO: implementar
    # TODO: type hint
    pass

def mostrar_saldo(usuario: Usuario) -> None:
    saldo: float = ServicoFinanceiro.calcular_saldo(usuario)
    print(f"\nSaldo atual: R$ {saldo}")

def registrar_transacao(usuario: Usuario):
    # TODO: implementar
    # TODO: type hint
    pass

def verificar_transacoes(usuario: Usuario): 
    # TODO: implementar
    # TODO: type hint
    pass

menu_principal()