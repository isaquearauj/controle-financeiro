from models.usuario import Usuario
from persistence.persistencia_json import PersistenciaJson
from services.servico_financeiro import ServicoFinanceiro
from pathlib import Path

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
        print(f"\n--- Usuário: {usuario.nome} ---")
        print("[1] Consultar saldo")
        print("[2] Nova transação")
        print("[3] Verificar transações")
        print("[0] Sair")

        escolha: str = input("Escolha uma opção: ")
        if escolha == '1':
            mostrar_saldo()
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
        nome = input("Digite seu nome: ")
        if usuario_ja_existe(nome):
            print("Usuário já existe!")
        else:
            novo = Usuario(id=0, nome=nome)
            PersistenciaJson.salvar(novo)
            print("Obrigado por se cadastrar em nosso sistema!")
            menu_usuario(novo)
            break

def usuario_ja_existe(nome) -> bool:
    path = Path(__file__).resolve().parents[1] / "data"

    for arquivo in path.iterdir():
        if arquivo.is_file() and arquivo.suffix == ".json":
            partes = arquivo.stem.split("_")
            if len(partes) >= 2:
                nome_arquivo = partes[0]
                if nome_arquivo.lower() == nome.lower():
                    return True
    return False

def selecionar_usuario_existente():
    pass

def mostrar_saldo(usuario: Usuario) -> None:
    saldo = ServicoFinanceiro.calcular_saldo(usuario)
    print(f"Saldo atual: {saldo}")

def registrar_transacao(usuario: Usuario):
    pass

def verificar_transacoes(usuario: Usuario): 
    pass



menu_principal()