import functools
from src.logger import get_logger

def handle_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = get_logger()
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error en {func.__name__}: {str(e)}", exc_info=True)
            print(f"Ocurrió un error: {str(e)}")
            return None
    return wrapper