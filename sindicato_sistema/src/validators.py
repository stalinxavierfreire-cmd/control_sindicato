import re

def validar_dni(dni: str) -> bool:
    """Valida que el DNI tenga 8 dígitos."""
    return bool(re.fullmatch(r"\d{8}", dni))

def validar_email(email: str) -> bool:
    """Valida el formato básico de email."""
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email))

def validar_telefono(telefono: str) -> bool:
    """Valida que el teléfono tenga entre 7 y 15 dígitos."""
    return bool(re.fullmatch(r"\d{7,15}", telefono))

def validar_estado(estado: str) -> bool:
    return estado in ("activo", "inactivo", "suspendido")