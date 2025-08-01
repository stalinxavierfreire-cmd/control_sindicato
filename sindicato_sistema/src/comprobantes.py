from datetime import datetime
from typing import List, Dict, Any
from src.database import DBConnection

def registrar_comprobante(tipo: str, monto: float, descripcion: str, socio_id: int = None) -> bool:
    fecha = datetime.now().strftime("%Y-%m-%d")
    try:
        with DBConnection() as cursor:
            cursor.execute(
                """INSERT INTO comprobantes 
                (tipo, monto, fecha, descripcion, socio_id)
                VALUES (?, ?, ?, ?, ?)""",
                (tipo, monto, fecha, descripcion, socio_id)
            )
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Error al registrar comprobante: {e}")
        return False

def listar_comprobantes(tipo: str = None, fecha_inicio: str = None, fecha_fin: str = None, socio_id: int = None) -> List[Dict[str, Any]]:
    conditions = []
    params = []
    if tipo:
        conditions.append("tipo = ?")
        params.append(tipo)
    if fecha_inicio:
        conditions.append("fecha >= ?")
        params.append(fecha_inicio)
    if fecha_fin:
        conditions.append("fecha <= ?")
        params.append(fecha_fin)
    if socio_id:
        conditions.append("socio_id = ?")
        params.append(socio_id)
    query = """SELECT c.*, s.nombres || ' ' || s.apellido1 || ' ' || s.apellido2 as socio_nombre
               FROM comprobantes c
               LEFT JOIN socios s ON c.socio_id = s.id"""
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    query += " ORDER BY c.fecha DESC"
    try:
        with DBConnection() as cursor:
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]
    except Exception as e:
        print(f"Error al listar comprobantes: {e}")
        return []