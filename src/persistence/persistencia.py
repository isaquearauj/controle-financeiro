import json
import csv
import os
from pathlib import Path
from datetime import datetime

from models.usuario import Usuario
from models.transacao import Transacao
from models.categoria import CategoriaReceita, CategoriaDespesa
from utils.decoradores import Decoradores

class Persistencia:
    @staticmethod
    @Decoradores.log_usuario("Dados salvos")
    def salvar(usuario: Usuario) -> None:
        path: Path = Path(__file__).resolve().parents[2] / "data"
        path.mkdir(parents=True, exist_ok=True)

        if usuario.id == 0:
            maior_id: int = 0
            for file in path.iterdir():
                if file.is_file() and file.suffix == ".json":
                    partes = file.stem.split("_")
                    if len(partes) >= 2 and partes[-1].isdigit():
                        id_atual = int(partes[-1])
                        maior_id = max(maior_id, id_atual)
            usuario.id = maior_id + 1

        nome_arquivo: str = f"{usuario.username.lower().replace(' ', '_')}_{usuario.id}.json"
        usuario_dict: dict = usuario.to_dict()

        with open(path / nome_arquivo, "w", encoding="utf-8") as file:
            json.dump(usuario_dict, file, ensure_ascii=False, indent=4)

    @staticmethod
    @Decoradores.log_acao("Dados carregados")
    def carregar(username: str) -> Usuario | None:
        path: Path = Path(__file__).resolve().parents[2] / "data"
        for arquivo in path.iterdir():
            if arquivo.is_file() and arquivo.name.startswith(username + "_"):
                id_str = arquivo.stem.split("_")[-1]
                if id_str.isdigit():
                    id_usuario = int(id_str)
            
                    with open(arquivo, "r", encoding="utf-8") as f:
                        dados = json.load(f)

                    usuario = Usuario(id=id_usuario, username=dados["username"])

                    for t in dados["transacoes"]:
                        try:
                            if t["tipo"] == "receita":
                                categoria = CategoriaReceita(t["categoria"])
                            else:
                                categoria = CategoriaDespesa(t["categoria"])
                            transacao = Transacao(
                            id=t["id"],
                            valor=t["valor"],
                            tipo=t["tipo"],
                            categoria=categoria,
                            data=datetime.fromisoformat(t["data"])
                        )
                            usuario.adicionar_transacao(transacao)
                        except Exception as e:
                            print(f"Erro ao carregar transação: {e}")

                    return usuario

    @staticmethod
    @Decoradores.log_usuario("Exportação CSV")
    def exportar_csv(usuario: Usuario) -> None:
        path: Path = Path(__file__).resolve().parents[2] / "reports"
        path.mkdir(parents=True, exist_ok=True)

        nome_arquivo: str = f"transacoes_{usuario.username.lower().replace(' ', '_')}_{usuario.id}.csv"
        cabecalho: list[str] = ["ID", "Tipo", "Valor", "Categoria", "Data"]

        with open(path / nome_arquivo, "w", encoding="utf-8", newline="") as file:
            writter = csv.writer(file)
            writter.writerow(cabecalho)
            for t in usuario.listar_transacoes():
                linha = [
                    t.id,
                    t.tipo,
                    f"{t.valor:.2f}",
                    t.categoria.value,
                    t.data.strftime("%d/%m/%Y %H:%M")
                ]
                writter.writerow(linha)
        
        print("Exportação concluída com sucesso!")
        os.startfile(path / nome_arquivo)
