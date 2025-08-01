from datetime import datetime
from typing import List, Dict, Any
from src.database import DBConnection

def validar_cedula_ecuador(cedula: str) -> bool:
    if len(cedula) != 10 or not cedula.isdigit():
        return False
    # Validación básica, puedes mejorar con el algoritmo oficial si lo requieres
    return True

def registrar_socio(nombres: str, apellido1: str, apellido2: str, cedula: str, telefono: str = "",
                    email: str = "", estado: str = "activo") -> bool:
    if not validar_cedula_ecuador(cedula):
        print("Cédula ecuatoriana inválida.")
        return False
    fecha_ingreso = datetime.now().strftime("%Y-%m-%d")
    try:
        with DBConnection() as cursor:
            cursor.execute(
                """INSERT INTO socios 
                (nombres, apellido1, apellido2, cedula, telefono, email, fecha_ingreso, estado)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (nombres, apellido1, apellido2, cedula, telefono, email, fecha_ingreso, estado)
            )
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Error al registrar socio: {e}")
        return False

def buscar_socio(nombres: str = None, apellido1: str = None, apellido2: str = None, cedula: str = None, estado: str = None) -> List[Dict[str, Any]]:
    conditions = []
    params = []
    if nombres:
        conditions.append("nombres LIKE ?")
        params.append(f"%{nombres}%")
    if apellido1:
        conditions.append("apellido1 LIKE ?")
        params.append(f"%{apellido1}%")
    if apellido2:
        conditions.append("apellido2 LIKE ?")
        params.append(f"%{apellido2}%")
    if cedula:
        conditions.append("cedula = ?")
        params.append(cedula)
    if estado:
        conditions.append("estado = ?")
        params.append(estado)
    query = "SELECT * FROM socios"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    try:
        with DBConnection() as cursor:
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]
    except Exception as e:
        print(f"Error al buscar socio: {e}")
        return []