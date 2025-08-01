import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_NAME = os.path.join(BASE_DIR, "db", "sindicato_ecuador.db")
LOG_FILE = os.path.join(BASE_DIR, "logs", "sindicato.log")
PDF_REPORTS_DIR = os.path.join(BASE_DIR, "reportes_pdf")
EXCEL_REPORTS_DIR = os.path.join(BASE_DIR, "reportes_excel")
LOG_TO_CONSOLE = True