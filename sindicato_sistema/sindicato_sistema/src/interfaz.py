from src.sistema import SistemaSindical
from src.asociados import GestionAsociados
from src.comprobantes import GestionComprobantes
from src.reportes import GeneradorReportes
from src.validators import validar_dni, validar_email, validar_telefono, validar_estado
from datetime import datetime

class InterfazUsuario:
    def __init__(self):
        self.sistema = SistemaSindical()
        self.gestion_asociados = GestionAsociados()
        self.gestion_comprobantes = GestionComprobantes()
        self.generador_reportes = GeneradorReportes()

    def mostrar_menu_principal(self):
        while True:
            print("\n" + "="*50)
            print(" SISTEMA DE CONTROL SINDICAL ".center(50, "="))
            print("="*50)
            print("\nMENÚ PRINCIPAL")
            print("1. Gestión de Asociados")
            print("2. Gestión de Comprobantes")
            print("3. Generación de Reportes")
            print("4. Configuración del Sistema")
            print("5. Salir")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                self.mostrar_menu_asociados()
            elif opcion == "2":
                self.mostrar_menu_comprobantes()
            elif opcion == "3":
                self.mostrar_menu_reportes()
            elif opcion == "4":
                self.mostrar_menu_configuracion()
            elif opcion == "5":
                print("\nSaliendo del sistema...")
                break
            else:
                print("\nOpción no válida. Intente nuevamente.")

    def mostrar_menu_asociados(self):
        while True:
            print("\n" + "="*50)
            print(" GESTIÓN DE ASOCIADOS ".center(50, "="))
            print("="*50)
            print("\nMENÚ DE ASOCIADOS")
            print("1. Registrar nuevo asociado")
            print("2. Editar asociado existente")
            print("3. Buscar asociados")
            print("4. Volver al menú principal")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                self.registrar_asociado()
            elif opcion == "2":
                self.editar_asociado()
            elif opcion == "3":
                self.buscar_asociados()
            elif opcion == "4":
                break
            else:
                print("\nOpción no válida. Intente nuevamente.")

    def registrar_asociado(self):
        print("\n" + "="*50)
        print(" REGISTRO DE NUEVO ASOCIADO ".center(50, "="))
        print("="*50)
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        dni = input("DNI (8 dígitos): ").strip()
        telefono = input("Teléfono (opcional): ").strip()
        email = input("Email (opcional): ").strip()
        if not nombre or not apellido or not dni:
            print("\nError: Nombre, apellido y DNI son campos obligatorios.")
            return
        if not validar_dni(dni):
            print("\nError: El DNI debe tener exactamente 8 números.")
            return
        if telefono and not validar_telefono(telefono):
            print("\nError: Teléfono debe tener entre 7 y 15 números.")
            return
        if email and not validar_email(email):
            print("\nError: Email inválido.")
            return
        if self.gestion_asociados.registrar_asociado(nombre, apellido, dni, telefono, email):
            print("\nAsociado registrado exitosamente.")
        else:
            print("\nError al registrar el asociado. Verifique los datos e intente nuevamente.")

    def editar_asociado(self):
        print("\n" + "="*50)
        print(" EDITAR ASOCIADO ".center(50, "="))
        print("="*50)
        dni = input("Ingrese el DNI del asociado a editar: ").strip()
        if not dni or not validar_dni(dni):
            print("\nError: Debe ingresar un DNI válido de 8 dígitos.")
            return
        asociados = self.gestion_asociados.buscar_asociados(dni=dni)
        if not asociados:
            print("\nNo se encontró ningún asociado con ese DNI.")
            return
        asociado = asociados[0]
        print("\nDatos actuales del asociado:")
        print(f"ID: {asociado['id']}")
        print(f"Nombre: {asociado['nombre']}")
        print(f"Apellido: {asociado['apellido']}")
        print(f"DNI: {asociado['dni']}")
        print(f"Teléfono: {asociado['telefono'] or 'No registrado'}")
        print(f"Email: {asociado['email'] or 'No registrado'}")
        print(f"Estado: {asociado['estado'].capitalize()}")
        print(f"Fecha de ingreso: {asociado['fecha_ingreso']}")
        print("\nIngrese los nuevos valores (deje en blanco para no modificar):")
        nombre = input(f"Nombre [{asociado['nombre']}]: ").strip()
        apellido = input(f"Apellido [{asociado['apellido']}]: ").strip()
        telefono = input(f"Teléfono [{asociado['telefono'] or ''}]: ").strip()
        email = input(f"Email [{asociado['email'] or ''}]: ").strip()
        estado = input(f"Estado (activo/inactivo/suspendido) [{asociado['estado']}]: ").strip().lower()
        if estado and not validar_estado(estado):
            print("\nError: Estado no válido. Debe ser 'activo', 'inactivo' o 'suspendido'.")
            return
        cambios = {}
        if nombre: cambios["nombre"] = nombre
        if apellido: cambios["apellido"] = apellido
        if telefono: cambios["telefono"] = telefono
        if email: cambios["email"] = email
        if estado: cambios["estado"] = estado
        if not cambios:
            print("\nNo se realizaron cambios.")
            return
        if self.gestion_asociados.editar_asociado(asociado["id"], **cambios):
            print("\nAsociado actualizado exitosamente.")
        else:
            print("\nError al actualizar el asociado. Intente nuevamente.")

    def buscar_asociados(self):
        print("\n" + "="*50)
        print(" BUSCAR ASOCIADOS ".center(50, "="))
        print("="*50)
        print("\nIngrese los criterios de búsqueda (deje en blanco para omitir):")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        dni = input("DNI: ").strip()
        estado = input("Estado (activo/inactivo/suspendido): ").strip().lower()
        asociados = self.gestion_asociados.buscar_asociados(
            nombre=nombre if nombre else None,
            apellido=apellido if apellido else None,
            dni=dni if dni else None,
            estado=estado if estado else None
        )
        if not asociados:
            print("\nNo se encontraron asociados con los criterios especificados.")
            return
        print("\n" + "="*100)
        print(" RESULTADOS DE BÚSQUEDA ".center(100, "="))
        print("="*100)
        print(f"{'ID':<5} {'Nombre':<20} {'Apellido':<20} {'DNI':<15} {'Teléfono':<15} {'Estado':<12} {'Ingreso':<10}")
        print("-"*100)
        for a in asociados:
            print(
                f"{a['id']:<5} {a['nombre']:<20} {a['apellido']:<20} {a['dni']:<15} "
                f"{a['telefono'] or '-':<15} {a['estado'].capitalize():<12} "
                f"{datetime.strptime(a['fecha_ingreso'], '%Y-%m-%d').strftime('%d/%m/%Y'):<10}"
            )
        print("="*100)
        input("\nPresione Enter para continuar...")

    def mostrar_menu_comprobantes(self):
        while True:
            print("\n" + "="*50)
            print(" GESTIÓN DE COMPROBANTES ".center(50, "="))
            print("="*50)
            print("\nMENÚ DE COMPROBANTES")
            print("1. Registrar comprobante de ingreso")
            print("2. Registrar comprobante de egreso")
            print("3. Consultar comprobantes")
            print("4. Ver resumen financiero")
            print("5. Volver al menú principal")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                self.registrar_comprobante("ingreso")
            elif opcion == "2":
                self.registrar_comprobante("egreso")
            elif opcion == "3":
                self.consultar_comprobantes()
            elif opcion == "4":
                self.ver_resumen_financiero()
            elif opcion == "5":
                break
            else:
                print("\nOpción no válida. Intente nuevamente.")

    def registrar_comprobante(self, tipo: str):
        tipo_str = "ingreso" if tipo == "ingreso" else "egreso"
        print("\n" + "="*50)
        print(f" REGISTRAR COMPROBANTE DE {tipo_str.upper()} ".center(50, "="))
        print("="*50)
        try:
            monto = float(input("Monto: ").strip())
            descripcion = input("Descripción: ").strip()
            asociado_id = None
            if tipo == "ingreso":
                dni = input("DNI del asociado (opcional): ").strip()
                if dni:
                    asociados = self.gestion_asociados.buscar_asociados(dni=dni)
                    if not asociados:
                        print(f"\nNo se encontró ningún asociado con DNI {dni}. Se registrará como ingreso general.")
                    else:
                        asociado_id = asociados[0]["id"]
            if not descripcion:
                print("\nError: La descripción es obligatoria.")
                return
            if self.gestion_comprobantes.registrar_comprobante(tipo, monto, descripcion, asociado_id):
                print(f"\nComprobante de {tipo_str} registrado exitosamente.")
            else:
                print(f"\nError al registrar el comprobante de {tipo_str}. Intente nuevamente.")
        except ValueError:
            print("\nError: El monto debe ser un número válido.")

    def consultar_comprobantes(self):
        print("\n" + "="*50)
        print(" CONSULTAR COMPROBANTES ".center(50, "="))
        print("="*50)
        print("\nIngrese los criterios de búsqueda (deje en blanco para omitir):")
        tipo = input("Tipo (ingreso/egreso): ").strip().lower()
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
        fecha_fin = input("Fecha de fin (YYYY-MM-DD): ").strip()
        dni = input("DNI del asociado: ").strip()
        asociado_id = None
        if dni:
            asociados = self.gestion_asociados.buscar_asociados(dni=dni)
            if not asociados:
                print(f"\nNo se encontró ningún asociado con DNI {dni}.")
                return
            asociado_id = asociados[0]["id"]
        comprobantes = self.gestion_comprobantes.obtener_comprobantes(
            tipo=tipo if tipo in ("ingreso", "egreso") else None,
            fecha_inicio=fecha_inicio if fecha_inicio else None,
            fecha_fin=fecha_fin if fecha_fin else None,
            asociado_id=asociado_id
        )
        if not comprobantes:
            print("\nNo se encontraron comprobantes con los criterios especificados.")
            return
        total_ingresos = sum(c["monto"] for c in comprobantes if c["tipo"] == "ingreso")
        total_egresos = sum(c["monto"] for c in comprobantes if c["tipo"] == "egreso")
        print("\n" + "="*120)
        print(" RESULTADOS DE BÚSQUEDA ".center(120, "="))
        print("="*120)
        print(f"{'Fecha':<12} {'Tipo':<10} {'Monto':<15} {'Descripción':<50} {'Asociado':<25} {'ID':<5}")
        print("-"*120)
        for c in comprobantes:
            print(
                f"{datetime.strptime(c['fecha'], '%Y-%m-%d').strftime('%d/%m/%Y'):<12} "
                f"{'Ingreso' if c['tipo'] == 'ingreso' else 'Egreso':<10} "
                f"{'$' + format(c['monto'], ',.2f'):<15}"
                f"{c['descripcion'][:47] + '...' if len(c['descripcion']) > 50 else c['descripcion']:<50} "
                f"{c['asociado_nombre'] or 'General':<25} "
                f"{c['id']:<5}"
            )
        print("-"*120)
        print(f"Total Ingresos: ${total_ingresos:,.2f}".rjust(119))
        print(f"Total Egresos: ${total_egresos:,.2f}".rjust(119))
        print(f"Balance: ${(total_ingresos - total_egresos):,.2f}".rjust(119))
        print("="*120)
        input("\nPresione Enter para continuar...")

    def ver_resumen_financiero(self):
        resumen = self.gestion_comprobantes.obtener_resumen_financiero()
        print("\n" + "="*50)
        print(" RESUMEN FINANCIERO ".center(50, "="))
        print("="*50)
        print(f"\n{'Total Ingresos:':<20} ${resumen['ingresos']:,.2f}")
        print(f"{'Total Egresos:':<20} ${resumen['egresos']:,.2f}")
        print(f"{'Balance:':<20} ${resumen['balance']:,.2f}")
        print("\n" + "="*50)
        input("\nPresione Enter para continuar...")

    def mostrar_menu_reportes(self):
        while True:
            print("\n" + "="*50)
            print(" GENERACIÓN DE REPORTES ".center(50, "="))
            print("="*50)
            print("\nMENÚ DE REPORTES")
            print("1. Reporte de Asociados (PDF)")
            print("2. Reporte de Asociados (Excel)")
            print("3. Reporte Financiero (PDF)")
            print("4. Reporte Financiero (Excel)")
            print("5. Volver al menú principal")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                self.generar_reporte_asociados_pdf()
            elif opcion == "2":
                self.generar_reporte_asociados_excel()
            elif opcion == "3":
                self.generar_reporte_financiero_pdf()
            elif opcion == "4":
                self.generar_reporte_financiero_excel()
            elif opcion == "5":
                break
            else:
                print("\nOpción no válida. Intente nuevamente.")

    def generar_reporte_asociados_pdf(self):
        print("\n" + "="*50)
        print(" REPORTE DE ASOCIADOS (PDF) ".center(50, "="))
        print("="*50)
        print("\nIngrese los criterios de filtro (deje en blanco para omitir):")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        dni = input("DNI: ").strip()
        estado = input("Estado (activo/inactivo/suspendido): ").strip().lower()
        filtros = {}
        if nombre: filtros["nombre"] = nombre
        if apellido: filtros["apellido"] = apellido
        if dni: filtros["dni"] = dni
        if estado: filtros["estado"] = estado
        ruta = self.generador_reportes.generar_reporte_asociados_pdf(filtros)
        if ruta:
            print(f"\nReporte generado exitosamente: {ruta}")
        else:
            print("\nError al generar el reporte. Verifique los datos e intente nuevamente.")
        input("\nPresione Enter para continuar...")

    def generar_reporte_asociados_excel(self):
        print("\n" + "="*50)
        print(" REPORTE DE ASOCIADOS (EXCEL) ".center(50, "="))
        print("="*50)
        print("\nIngrese los criterios de filtro (deje en blanco para omitir):")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        dni = input("DNI: ").strip()
        estado = input("Estado (activo/inactivo/suspendido): ").strip().lower()
        filtros = {}
        if nombre: filtros["nombre"] = nombre
        if apellido: filtros["apellido"] = apellido
        if dni: filtros["dni"] = dni
        if estado: filtros["estado"] = estado
        ruta = self.generador_reportes.generar_reporte_asociados_excel(filtros)
        if ruta:
            print(f"\nReporte generado exitosamente: {ruta}")
        else:
            print("\nError al generar el reporte. Verifique los datos e intente nuevamente.")
        input("\nPresione Enter para continuar...")

    def generar_reporte_financiero_pdf(self):
        print("\n" + "="*50)
        print(" REPORTE FINANCIERO (PDF) ".center(50, "="))
        print("="*50)
        print("\nIngrese los criterios de filtro (deje en blanco para omitir):")
        tipo = input("Tipo (ingreso/egreso): ").strip().lower()
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
        fecha_fin = input("Fecha de fin (YYYY-MM-DD): ").strip()
        dni = input("DNI del asociado: ").strip()
        asociado_id = None
        if dni:
            asociados = self.gestion_asociados.buscar_asociados(dni=dni)
            if not asociados:
                print(f"\nNo se encontró ningún asociado con DNI {dni}.")
                return
            asociado_id = asociados[0]["id"]
        filtros = {}
        if tipo in ("ingreso", "egreso"): filtros["tipo"] = tipo
        if fecha_inicio: filtros["fecha_inicio"] = fecha_inicio
        if fecha_fin: filtros["fecha_fin"] = fecha_fin
        if asociado_id: filtros["asociado_id"] = asociado_id
        ruta = self.generador_reportes.generar_reporte_financiero_pdf(filtros)
        if ruta:
            print(f"\nReporte generado exitosamente: {ruta}")
        else:
            print("\nError al generar el reporte. Verifique los datos e intente nuevamente.")
        input("\nPresione Enter para continuar...")

    def generar_reporte_financiero_excel(self):
        print("\n" + "="*50)
        print(" REPORTE FINANCIERO (EXCEL) ".center(50, "="))
        print("="*50)
        print("\nIngrese los criterios de filtro (deje en blanco para omitir):")
        tipo = input("Tipo (ingreso/egreso): ").strip().lower()
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
        fecha_fin = input("Fecha de fin (YYYY-MM-DD): ").strip()
        dni = input("DNI del asociado: ").strip()
        asociado_id = None
        if dni:
            asociados = self.gestion_asociados.buscar_asociados(dni=dni)
            if not asociados:
                print(f"\nNo se encontró ningún asociado con DNI {dni}.")
                return
            asociado_id = asociados[0]["id"]
        filtros = {}
        if tipo in ("ingreso", "egreso"): filtros["tipo"] = tipo
        if fecha_inicio: filtros["fecha_inicio"] = fecha_inicio
        if fecha_fin: filtros["fecha_fin"] = fecha_fin
        if asociado_id: filtros["asociado_id"] = asociado_id
        ruta = self.generador_reportes.generar_reporte_financiero_excel(filtros)
        if ruta:
            print(f"\nReporte generado exitosamente: {ruta}")
        else:
            print("\nError al generar el reporte. Verifique los datos e intente nuevamente.")
        input("\nPresione Enter para continuar...")

    def mostrar_menu_configuracion(self):
        while True:
            print("\n" + "="*50)
            print(" CONFIGURACIÓN DEL SISTEMA ".center(50, "="))
            print("="*50)
            print("\nMENÚ DE CONFIGURACIÓN")
            print("1. Ver configuración actual")
            print("2. Modificar configuración")
            print("3. Volver al menú principal")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                self.ver_configuracion()
            elif opcion == "2":
                self.modificar_configuracion()
            elif opcion == "3":
                break
            else:
                print("\nOpción no válida. Intente nuevamente.")

    def ver_configuracion(self):
        configs = [
            ("nombre_sindicato", "Nombre del Sindicato"),
            ("direccion", "Dirección"),
            ("telefono", "Teléfono"),
            ("logo_path", "Ruta del Logo"),
            ("cuota_basica", "Cuota Básica")
        ]
        print("\n" + "="*50)
        print(" CONFIGURACIÓN ACTUAL ".center(50, "="))
        print("="*50)
        for clave, descripcion in configs:
            valor = self.sistema.obtener_configuracion(clave)
            print(f"\n{descripcion}: {valor or 'No configurado'}")
        print("\n" + "="*50)
        input("\nPresione Enter para continuar...")

    def modificar_configuracion(self):
        configs = [
            ("nombre_sindicato", "Nombre del Sindicato"),
            ("direccion", "Dirección"),
            ("telefono", "Teléfono"),
            ("logo_path", "Ruta del Logo"),
            ("cuota_basica", "Cuota Básica")
        ]
        print("\n" + "="*50)
        print(" MODIFICAR CONFIGURACIÓN ".center(50, "="))
        print("="*50)
        print("\nSeleccione el parámetro a modificar:")
        for i, (clave, descripcion) in enumerate(configs, start=1):
            print(f"{i}. {descripcion}")
        print(f"{len(configs)+1}. Cancelar")
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if opcion == len(configs)+1:
                return
            elif 1 <= opcion <= len(configs):
                clave, descripcion = configs[opcion-1]
                valor_actual = self.sistema.obtener_configuracion(clave)
                print(f"\n{descripcion}")
                print(f"Valor actual: {valor_actual or 'No configurado'}")
                nuevo_valor = input("Nuevo valor: ").strip()
                if nuevo_valor:
                    if clave == "cuota_basica":
                        try:
                            float(nuevo_valor)
                        except ValueError:
                            print("\nError: La cuota básica debe ser un número válido.")
                            return
                    if self.sistema.actualizar_configuracion(clave, nuevo_valor):
                        print("\nConfiguración actualizada exitosamente.")
                    else:
                        print("\nError al actualizar la configuración.")
                else:
                    print("\nNo se realizaron cambios.")
            else:
                print("\nOpción no válida.")
        except ValueError:
            print("\nError: Debe ingresar un número válido.")
        input("\nPresione Enter para continuar...")