from src.asociados import registrar_socio, buscar_socio
from src.comprobantes import registrar_comprobante, listar_comprobantes

def menu_principal():
    while True:
        print("\n=== Menú Principal (Ecuador) ===")
        print("1. Registrar socio")
        print("2. Buscar socio")
        print("3. Registrar comprobante")
        print("4. Listar comprobantes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombres = input("Nombres: ")
            apellido1 = input("Primer apellido: ")
            apellido2 = input("Segundo apellido: ")
            cedula = input("Cédula: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            if registrar_socio(nombres, apellido1, apellido2, cedula, telefono, email):
                print("Socio registrado con éxito.")
            else:
                print("Error al registrar socio.")
        elif opcion == "2":
            nombres = input("Nombres (opcional): ")
            apellido1 = input("Primer apellido (opcional): ")
            apellido2 = input("Segundo apellido (opcional): ")
            cedula = input("Cédula (opcional): ")
            resultados = buscar_socio(nombres or None, apellido1 or None, apellido2 or None, cedula or None)
            if not resultados:
                print("No se encontraron socios.")
            else:
                for r in resultados:
                    print(r)
        elif opcion == "3":
            tipo = input("Tipo (ingreso/egreso/aporte): ")
            monto = float(input("Monto: "))
            descripcion = input("Descripción: ")
            socio_id = input("ID de socio (opcional): ")
            if socio_id.strip() == "":
                socio_id = None
            else:
                socio_id = int(socio_id)
            if registrar_comprobante(tipo, monto, descripcion, socio_id):
                print("Comprobante registrado con éxito.")
            else:
                print("Error al registrar comprobante.")
        elif opcion == "4":
            comprobantes = listar_comprobantes()
            if not comprobantes:
                print("No hay comprobantes registrados.")
            else:
                for c in comprobantes:
                    print(c)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")