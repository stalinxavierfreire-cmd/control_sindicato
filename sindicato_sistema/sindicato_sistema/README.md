# Sistema de Gestión Sindical – Ecuador

Este sistema permite la gestión básica de socios, comprobantes y registros para un sindicato en Ecuador.

## Requisitos

- Python 3.x
- No requiere librerías externas (solo `sqlite3` y módulos estándar).

## Estructura

- `main.py`: archivo principal para ejecutar el sistema.
- `config.py`: configuración de rutas y base de datos.
- `src/database.py`: conexión y creación de tablas en la base de datos.
- `src/asociados.py`: manejo de socios (registro, búsqueda).
- `src/comprobantes.py`: manejo de comprobantes.
- `src/menu.py`: menú interactivo por consola.

## Uso

1. Ejecuta el sistema:

   ```bash
   python main.py
   ```

2. Sigue las instrucciones del menú para:
    - Registrar socios (con validación básica de cédula ecuatoriana)
    - Buscar socios
    - Registrar comprobantes (ingreso, egreso, aporte)
    - Listar comprobantes

## Notas

- El sistema crea automáticamente las carpetas y la base de datos al ejecutarse por primera vez.
- Puedes adaptar y expandir las funciones según las necesidades de tu organización.
- El sistema usa terminología y campos estándar para Ecuador (dos apellidos, cédula, etc).
