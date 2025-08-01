import sqlite3
from config import DATABASE_NAME

class DBConnection:
    def __init__(self, db_name: str = DATABASE_NAME):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombres TEXT NOT NULL,
            apellido1 TEXT NOT NULL,
            apellido2 TEXT NOT NULL,
            cedula TEXT UNIQUE NOT NULL,
            telefono TEXT,
            email TEXT,
            fecha_ingreso TEXT NOT NULL,
            estado TEXT NOT NULL CHECK(estado IN ('activo', 'pasivo', 'retirado', 'fallecido'))
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comprobantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL CHECK(tipo IN ('ingreso', 'egreso', 'aporte')),
            monto REAL NOT NULL,
            fecha TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            socio_id INTEGER,
            FOREIGN KEY(socio_id) REFERENCES socios(id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS configuracion (
            clave TEXT PRIMARY KEY,
            valor TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()