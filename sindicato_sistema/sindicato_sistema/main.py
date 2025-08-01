import os
from src.database import init_db

def crear_carpetas():
    for carpeta in ["db", "logs", "reportes_pdf", "reportes_excel", "src"]:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

if __name__ == "__main__":
    crear_carpetas()
    init_db()
    from src.menu import menu_principal
    menu_principal()