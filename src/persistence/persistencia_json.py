import json
from pathlib import Path

from models.usuario import Usuario
from utils.decoradores import Decoradores

class PersistenciaJson:
    @staticmethod
    @Decoradores.log_acao
    def salvar(usuario: Usuario) -> None:
        path: Path = Path(__file__).resolve().parents[2] / "data"
        path.mkdir(parents=True, exist_ok=True)

        maior_id: int = 0
        for file in path.iterdir():
            if file.is_file() and file.suffix == ".json":
                file_name: str = file.stem
                partes: list[str] = file_name.split("_")
                if len(partes) >= 2 and partes[-1].isdigit():
                    id_atual: int = int(partes[-1])
                    maior_id = max(maior_id, id_atual)

        proximo_id: int = maior_id + 1
        nome_novo_arquivo: str = f"{usuario.username.lower().replace(' ', '_')}_{proximo_id}.json"

        usuario.id = proximo_id
        usuario_dict: dict = usuario.to_dict()

        with open(path / nome_novo_arquivo, "w", encoding="utf-8") as file:
            json.dump(usuario_dict, file, ensure_ascii=False, indent=4)

    @staticmethod
    @Decoradores.log_acao
    def carregar(id: int) -> None:
        pass

    @staticmethod
    @Decoradores.log_acao
    def exportar_csv() -> None:
        pass