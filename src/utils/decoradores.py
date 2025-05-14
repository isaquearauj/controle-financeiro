from functools import wraps
from datetime import datetime
from pathlib import Path

class Decoradores:
    @staticmethod
    def log_acao(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            resultado = func(*args, **kwargs)

            log_path = Path(__file__).resolve().parents[2] / "logs" / "acoes.log"
            log_path.parent.mkdir(parents=True, exist_ok=True)

            log_message = f"{datetime.now().isoformat()} - {func.__name__} executado\n"

            with log_path.open("a", encoding="utf-8") as log_file:
                log_file.write(log_message)

            return resultado
        return wrapper