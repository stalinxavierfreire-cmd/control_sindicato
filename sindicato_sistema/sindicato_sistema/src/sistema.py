import os
from src.db import DBConnection
from src.decorators import handle_errors

class SistemaSindical:
    def __init__(self):
        self._inicializar_db()

    def _inicializar_db(self):
        queries = [
            """CREATE TABLE IF NOT EXISTS asociados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                dni TEXT UNIQUE NOT NULL,
                telefono TEXT,
                email TEXT,
                fecha_ingreso TEXT NOT NULL,
                estado TEXT NOT NULL CHECK(estado IN ('activo', 'inactivo', 'suspendido'))
            )""",
            """CREATE TABLE IF NOT EXISTS comprobantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL CHECK(tipo IN ('ingreso', 'egreso')),
                monto REAL NOT NULL,
                fecha TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                asociado_id INTEGER,
                FOREIGN KEY(asociado_id) REFERENCES asociados(id)
            )""",
            """CREATE TABLE IF NOT EXISTS configuracion (
                clave TEXT PRIMARY KEY,
                valor TEXT NOT NULL
            )"""
        ]

        with DBConnection() as cursor:
            for query in queries:
                cursor.execute(query)

        # Configuración inicial
        configs = [
            ("nombre_sindicato", "Sindicato Ejemplo"),
            ("direccion", "Calle Falsa 123"),
            ("telefono", "555-1234"),
            ("logo_path", ""),
            ("cuota_basica", "1000.00")
        ]

        with DBConnection() as cursor:
            for clave, valor in configs:
                try:
                    cursor.execute(
                        "INSERT INTO configuracion (clave, valor) VALUES (?, ?)",
                        (clave, valor)
                    )
                except Exception:
                    pass

    @handle_errors
    def obtener_configuracion(self, clave: str):
        with DBConnection() as cursor:
            cursor.execute("SELECT valor FROM configuracion WHERE clave = ?", (clave,))
            result = cursor.fetchone()
            return result["valor"] if result else None

    @handle_errors
    def actualizar_configuracion(self, clave: str, valor: str) -> bool:
        with DBConnection() as cursor:
            cursor.execute(
                "INSERT OR REPLACE INTO configuracion (clave, valor) VALUES (?, ?)",
                (clave, valor)
            )
            return cursor.rowcount > 0
