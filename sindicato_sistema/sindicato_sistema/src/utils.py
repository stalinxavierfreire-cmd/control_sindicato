from datetime import datetime

def str_to_date(date_str: str, fmt: str = "%Y-%m-%d") -> datetime:
    return datetime.strptime(date_str, fmt)

def date_to_str(date_obj: datetime, fmt: str = "%Y-%m-%d") -> str:
    return date_obj.strftime(fmt)

def input_opcional(texto: str, valor_actual: str = "") -> str:
    entrada = input(texto)
    return entrada.strip() if entrada.strip() else valor_actual