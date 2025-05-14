import json
from models.usuario import Usuario
from utils.decoradores import Decoradores
from pathlib import Path


class PersistenciaJson:
    @staticmethod
    @Decoradores.log_acao
    def salvar(usuario: Usuario):
        path = Path(__file__).resolve().parents[2] / "data"
        path.mkdir(parents=True, exist_ok=True)

        maior_id = 0
        for arquivo in path.iterdir():
            if arquivo.is_file() and arquivo.suffix == ".json":
                nome = arquivo.stem
                partes = nome.split("_")
                if len(partes) >= 2 and partes[-1].isdigit():
                    id_atual = int(partes[-1])
                    maior_id = max(maior_id, id_atual)

        proximo_id = maior_id + 1
        nome_arquivo = f"{usuario.nome.lower().replace(" ", "_")}_{proximo_id}.json"

        usuario.id = proximo_id
        usuario_dict = usuario.to_dict()

        with open(path / nome_arquivo, "w", encoding="utf-8") as file:
            json.dump(usuario_dict, file, ensure_ascii=False, indent=4)

        return

    @staticmethod
    @Decoradores.log_acao
    def carregar(id: int):
        pass

    @staticmethod
    @Decoradores.log_acao
    def exportar_csv():
        pass