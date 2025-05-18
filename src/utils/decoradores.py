from functools import wraps
from datetime import datetime
from pathlib import Path

class Decoradores:

    @staticmethod
    def log_acao(acao: str):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                log_path = Path(__file__).resolve().parents[2] / "logs" / "acoes.log"
                log_path.parent.mkdir(parents=True, exist_ok=True)

                log_message = f"{datetime.now().isoformat()} - {acao}\n"
                with log_path.open("a", encoding="utf-8") as log_file:
                    log_file.write(log_message)

                return func(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def log_usuario(acao: str):
        def decorator(func):
            @wraps(func)
            def wrapper(usuario, *args, **kwargs):
                log_path = Path(__file__).resolve().parents[2] / "logs" / "acoes.log"
                log_path.parent.mkdir(parents=True, exist_ok=True)

                log_message = (
                    f"{datetime.now().isoformat()} - {acao} por {usuario.username}\n"
                )

                with log_path.open("a", encoding="utf-8") as log_file:
                    log_file.write(log_message)

                return func(usuario, *args, **kwargs)
            return wrapper
        return decorator