from src.asociados import registrar_socio, buscar_socio
from src.comprobantes import registrar_comprobante, listar_comprobantes

def menu_principal():
    while True:
        print("\n=== Menú Principal (Ecuador) ===")
        print("1. Registrar socio")
        print("2. Buscar socio")
        print("3. Registrar comprobante de ingreso")
        print("4. Registrar comprobante de egreso")
        print("5. Listar comprobantes de ingreso")
        print("6. Listar comprobantes de egreso")
        print("7. Generar comprobantes PDF")
        print("8. Salir")
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
            tipo = "ingreso"
            cedula = input("Cédula del socio (obligatoria): ").strip()
            if not cedula:
                print("Debe ingresar la cédula del socio.")
                continue
            socios = buscar_socio(cedula=cedula)
            if not socios:
                print("No se encontró ningún socio con esa cédula. Debe registrar el socio primero.")
                continue
            socio_id = socios[0]['id']
            monto = float(input("Monto: "))
            descripcion = input("Descripción: ")
            if registrar_comprobante(tipo, monto, descripcion, socio_id):
                print("Comprobante de ingreso registrado con éxito.")
            else:
                print("Error al registrar comprobante de ingreso.")
        elif opcion == "4":
            tipo = "egreso"
            cedula = input("Cédula del socio (obligatoria): ").strip()
            if not cedula:
                print("Debe ingresar la cédula del socio.")
                continue
            socios = buscar_socio(cedula=cedula)
            if not socios:
                print("No se encontró ningún socio con esa cédula. Debe registrar el socio primero.")
                continue
            socio_id = socios[0]['id']
            monto = float(input("Monto: "))
            descripcion = input("Descripción: ")
            if registrar_comprobante(tipo, monto, descripcion, socio_id):
                print("Comprobante de egreso registrado con éxito.")
            else:
                print("Error al registrar comprobante de egreso.")
        elif opcion == "5":
            cedula = input("Cédula del socio: ").strip()
            if not cedula:
                print("Debe ingresar la cédula del socio.")
                continue
            socios = buscar_socio(cedula=cedula)
            if not socios:
                print("No se encontró ningún socio con esa cédula.")
                continue
            socio_id = socios[0]['id']
            socio_nombre = f"{socios[0]['nombres']} {socios[0]['apellido1']} {socios[0]['apellido2']}"
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
            fecha_fin = input("Fecha de finalización (YYYY-MM-DD): ").strip()
            if not fecha_inicio or not fecha_fin:
                print("Debe ingresar tanto la fecha de inicio como la de finalización.")
                continue
            comprobantes = listar_comprobantes(tipo="ingreso", fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, socio_id=socio_id)
            if not comprobantes:
                print("No hay comprobantes de ingreso registrados en ese rango para ese socio.")
            else:
                print(f"\nComprobantes de ingreso para: {socio_nombre} ({cedula})")
                print("-" * 120)
                print("{:<5} {:<18} {:<12} {:<10} {:<12} {:<35} {:<10}".format(
                    "ID", "No.Comprobante", "Fecha", "Monto", "Tipo", "Descripción", "Socio ID"
                ))
                print("-" * 120)
                for c in comprobantes:
                    print("{:<5} {:<18} {:<12} {:<10.2f} {:<12} {:<35} {:<10}".format(
                        c['id'],
                        c.get('numero_comprobante', 'N/A'),
                        c['fecha'],
                        c['monto'],
                        c['tipo'].capitalize(),
                        c['descripcion'][:34],
                        c['socio_id']
                    ))
                print("-" * 120)
        elif opcion == "6":
            cedula = input("Cédula del socio: ").strip()
            if not cedula:
                print("Debe ingresar la cédula del socio.")
                continue
            socios = buscar_socio(cedula=cedula)
            if not socios:
                print("No se encontró ningún socio con esa cédula.")
                continue
            socio_id = socios[0]['id']
            socio_nombre = f"{socios[0]['nombres']} {socios[0]['apellido1']} {socios[0]['apellido2']}"
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
            fecha_fin = input("Fecha de finalización (YYYY-MM-DD): ").strip()
            if not fecha_inicio or not fecha_fin:
                print("Debe ingresar tanto la fecha de inicio como la de finalización.")
                continue
            comprobantes = listar_comprobantes(tipo="egreso", fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, socio_id=socio_id)
            if not comprobantes:
                print("No hay comprobantes de egreso registrados en ese rango para ese socio.")
            else:
                print(f"\nComprobantes de egreso para: {socio_nombre} ({cedula})")
                print("-" * 120)
                print("{:<5} {:<18} {:<12} {:<10} {:<12} {:<35} {:<10}".format(
                    "ID", "No.Comprobante", "Fecha", "Monto", "Tipo", "Descripción", "Socio ID"
                ))
                print("-" * 120)
                for c in comprobantes:
                    print("{:<5} {:<18} {:<12} {:<10.2f} {:<12} {:<35} {:<10}".format(
                        c['id'],
                        c.get('numero_comprobante', 'N/A'),
                        c['fecha'],
                        c['monto'],
                        c['tipo'].capitalize(),
                        c['descripcion'][:34],
                        c['socio_id']
                    ))
                print("-" * 120)
        elif opcion == "7":
            print("Funcionalidad para generar comprobantes PDF no implementada en este menú.")
            # Aquí puedes agregar la llamada a la función de generación de PDF si está disponible
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")