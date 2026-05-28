from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from services.Afiliaciones import (
    crear_afiliacion,
    obtener_todas_afiliaciones,
    obtener_afiliaciones_por_candidato,
    actualizar_estado_afiliacion,
    eliminar_afiliacion,
    actualizar_afiliacion,
)
from services.Candidatos import obtener_todos_candidatos, list_candidatos
from services.Contratos import list_contratados
from utils.ui import clear_screen
from utils.status import set_status

console = Console()


def gestionar_afiliaciones():
    """Menú principal de gestión de afiliaciones"""
    while True:
        clear_screen()
        console.rule("[bold cyan]Gestión de Afiliaciones")
        console.print(
            Panel(
                "[1] - Ver todas las afiliaciones\n"
                "[2] - Crear afiliación\n"
                "[3] - Ver afiliaciones por empleado\n"
                "[4] - Modificar afiliación\n"
                "[5] - Actualizar estado\n"
                "[6] - Eliminar afiliación\n"
                "[7] - Volver",
                title="Opciones",
            )
        )
        opcion = console.input("Seleccione opción: ").strip()

        if opcion == "1":
            ver_todas_afiliaciones()
        elif opcion == "2":
            crear_nueva_afiliacion()
        elif opcion == "3":
            ver_afiliaciones_empleado()
        elif opcion == "4":
            modificar_afiliacion()
        elif opcion == "5":
            actualizar_una_afiliacion()
        elif opcion == "6":
            eliminar_una_afiliacion()
        elif opcion == "7":
            break
        else:
            console.print("[red]Opción inválida[/red]")
            console.input("Presione Enter para continuar...")


def ver_todas_afiliaciones():
    """Ver todas las afiliaciones agrupadas por empleado"""
    clear_screen()
    console.rule("[bold cyan]Todas las Afiliaciones")
    afiliaciones = obtener_todas_afiliaciones()

    if not afiliaciones:
        console.print("[yellow]No hay afiliaciones registradas[/yellow]")
        console.input("Presione Enter para continuar...")
        return

    # Group by employee
    from collections import defaultdict
    grouped = defaultdict(lambda: {"EPS": {}, "Fondo de Pensiones": {}, "ARL": {}, "Caja de Compensación": {}})
    
    for afil in afiliaciones:
        nombre = afil[7]  # nombre
        tipo = afil[2]  # tipo
        entidad = str(afil[3])
        numero = str(afil[4])
        estado = afil[6]
        afil_id = afil[0]
        
        if tipo in grouped[nombre]:
            grouped[nombre][tipo] = {"id": afil_id, "entidad": entidad, "numero": numero, "estado": estado}

    table = Table(title="Afiliaciones de Seguridad Social por Empleado")
    table.add_column("ID", style="cyan", width=3)
    table.add_column("Empleado", style="magenta")
    table.add_column("EPS", style="green")
    table.add_column("EPS #", style="green")
    table.add_column("Pensión", style="magenta")
    table.add_column("Pensión #", style="magenta")
    table.add_column("ARL", style="yellow")
    table.add_column("ARL #", style="yellow")
    table.add_column("Caja", style="blue")
    table.add_column("Caja #", style="blue")

    for nombre, AFIL in sorted(grouped.items()):
        eps = AFIL.get("EPS", {})
        pen = AFIL.get("Fondo de Pensiones", {})
        arl = AFIL.get("ARL", {})
        caja = AFIL.get("Caja de Compensación", {})
        
        # Get first ID for reference
        first_id = eps.get("id") or pen.get("id") or arl.get("id") or caja.get("id") or "-"
        
        table.add_row(
            str(first_id),
            nombre,
            eps.get("entidad", "-"),
            eps.get("numero", "-"),
            pen.get("entidad", "-"),
            pen.get("numero", "-"),
            arl.get("entidad", "-"),
            arl.get("numero", "-"),
            caja.get("entidad", "-"),
            caja.get("numero", "-"),
        )

    console.print(table)
    console.input("Presione Enter para continuar...")


def crear_nueva_afiliacion():
    """Crear afiliación completa - las 4 protecciones sociales simultáneamente"""
    clear_screen()
    console.rule("[bold cyan]Crear Afiliación completa")

    # Only show employees that have contracts
    contratados = list_contratados()
    if not contratados:
        console.print("[red]No hay empleados contratados para afiliar[/red]")
        console.input("Presione Enter para continuar...")
        return

    console.print("\n[bold]Empleados contratados disponibles:[/bold]")
    for i, cand in enumerate(contratados, 1):
        console.print(f"{i}. {cand['nombre']} - {cand['tipo']}")

    try:
        num = int(console.input("\nSeleccione número de empleado: ").strip())
        if 1 <= num <= len(contratados):
            candidato_id = contratados[num - 1]["id"]
            nombre_emp = contratados[num - 1]["nombre"]

            console.print(f"\n[bold]Afiliaciones para {nombre_emp}:[/bold]")
            console.print("[cyan]Debe registrar las 4 protecciones sociales:[/cyan]")
            
            # EPS
            console.print("\n[bold]1. EPS (Salud):[/bold]")
            eps_entidad = console.input("  Entidad EPS: ").strip()
            eps_num = console.input("  Número de afiliación EPS: ").strip()
            
            # Fondo de Pensiones
            console.print("\n[bold]2. Fondo de Pensiones:[/bold]")
            pension_entidad = console.input("  Entidad FONDO DE PENSIONES: ").strip()
            pension_num = console.input("  Número de afiliación: ").strip()
            
            # ARL
            console.print("\n[bold]3. ARL (Riesgos Laborales):[/bold]")
            arl_entidad = console.input("  Entidad ARL: ").strip()
            arl_num = console.input("  Número de afiliación ARL: ").strip()
            
            # Caja de Compensación
            console.print("\n[bold]4. Caja de Compensación:[/bold]")
            caja_entidad = console.input("  Entidad Caja de Compensación: ").strip()
            caja_num = console.input("  Número de afiliación: ").strip()

            # Create all 4 affiliations
            if eps_entidad and eps_num:
                crear_afiliacion(candidato_id, "EPS", eps_entidad, eps_num)
            if pension_entidad and pension_num:
                crear_afiliacion(candidato_id, "Fondo de Pensiones", pension_entidad, pension_num)
            if arl_entidad and arl_num:
                crear_afiliacion(candidato_id, "ARL", arl_entidad, arl_num)
            if caja_entidad and caja_num:
                crear_afiliacion(candidato_id, "Caja de Compensación", caja_entidad, caja_num)
            
            set_status("Afiliaciones creadas exitosamente")
            console.print(
                Panel("[green]✓ Afiliaciones completas registradas para " + nombre_emp + "[/green]", style="green")
            )
        else:
            console.print("[red]Número inválido[/red]")
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def ver_afiliaciones_empleado():
    """Ver afiliaciones de un empleado"""
    clear_screen()
    console.rule("[bold cyan]Afiliaciones por Empleado")

    # Only show employees that have contracts
    contratados = list_contratados()
    if not contratados:
        console.print("[red]No hay empleados contratados[/red]")
        console.input("Presione Enter para continuar...")
        return

    console.print("\n[bold]Empleados contratados:[/bold]")
    for i, cand in enumerate(contratados, 1):
        console.print(f"{i}. {cand['nombre']}")

    try:
        num = int(console.input("\nSeleccione número: ").strip())
        if 1 <= num <= len(contratados):
            candidato_id = contratados[num - 1]["id"]
            nombre_empleado = contratados[num - 1]["nombre"]
            afiliaciones = obtener_afiliaciones_por_candidato(candidato_id)

            if not afiliaciones:
                console.print(
                    "[yellow]No hay afiliaciones para este empleado[/yellow]"
                )
            else:
                table = Table(
                    title=f"Afiliaciones de {nombre_empleado}"
                )
                table.add_column("ID", style="cyan")
                table.add_column("Tipo", style="green")
                table.add_column("Entidad", style="yellow")
                table.add_column("Número", style="blue")
                table.add_column("Estado", style="cyan")

                for afil in afiliaciones:
                    table.add_row(
                        str(afil[0]),
                        str(afil[2]),
                        str(afil[3]),
                        str(afil[4]),
                        afil[6],
                    )

                console.print(table)
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def modificar_afiliacion():
    """Modificar entidad y/o número de una afiliación"""
    clear_screen()
    console.rule("[bold cyan]Modificar Afiliación")
    
    # First show all affiliations grouped by employee
    afiliaciones = obtener_todas_afiliaciones()
    if not afiliaciones:
        console.print("[yellow]No hay afiliaciones registradas[/yellow]")
        console.input("Presione Enter para continuar...")
        return
    
    # Group by employee
    from collections import defaultdict
    grouped = defaultdict(lambda: {"EPS": {}, "Fondo de Pensiones": {}, "ARL": {}, "Caja de Compensación": {}})
    
    for afil in afiliaciones:
        nombre = afil[7]  # nombre
        tipo = afil[2]  # tipo
        entidad = str(afil[3])
        numero = str(afil[4])
        afil_id = afil[0]
        
        if tipo in grouped[nombre]:
            grouped[nombre][tipo] = {"id": afil_id, "entidad": entidad, "numero": numero}

    # Show table grouped by employee
    table = Table(title="Afiliaciones - Seleccione por ID")
    table.add_column("ID", style="cyan", width=3)
    table.add_column("Empleado", style="magenta")
    table.add_column("EPS", style="green")
    table.add_column("EPS #", style="green")
    table.add_column("Pensión", style="magenta")
    table.add_column("Pensión #", style="magenta")
    table.add_column("ARL", style="yellow")
    table.add_column("ARL #", style="yellow")
    table.add_column("Caja", style="blue")
    table.add_column("Caja #", style="blue")

    for nombre, AFIL in sorted(grouped.items()):
        eps = AFIL.get("EPS", {})
        pen = AFIL.get("Fondo de Pensiones", {})
        arl = AFIL.get("ARL", {})
        caja = AFIL.get("Caja de Compensación", {})
        
        # Get first ID for reference
        first_id = eps.get("id") or pen.get("id") or arl.get("id") or caja.get("id") or "-"
        
        table.add_row(
            str(first_id),
            nombre,
            eps.get("entidad", "-"),
            eps.get("numero", "-"),
            pen.get("entidad", "-"),
            pen.get("numero", "-"),
            arl.get("entidad", "-"),
            arl.get("numero", "-"),
            caja.get("entidad", "-"),
            caja.get("numero", "-"),
        )
    console.print(table)
    
    # Primero pedir ID del empleado
    try:
        afil_id = int(console.input("\nIngrese ID de la afiliación del empleado: ").strip())
        
        # Encontrar la afiliación seleccionada para obtener el empleado
        afil_found = None
        for afil in afiliaciones:
            if afil[0] == afil_id:
                afil_found = afil
                break
        
        if not afil_found:
            console.print("[red]Afiliación no encontrada[/red]")
            console.input("Presione Enter para continuar...")
            return
        
        empleado_nombre = afil_found[7]
        candidato_id = afil_found[1]
        
        # Ahora preguntar qué tipo de afiliación modificar
        console.print(f"\n[bold]Afiliaciones de {empleado_nombre}:[/bold]")
        console.print("\n[cyan]Seleccione el tipo de afiliación a modificar:[/cyan]")
        console.print("[1] - EPS (Salud)")
        console.print("[2] - Fondo de Pensiones (Pensión)")
        console.print("[3] - ARL (Riesgos Laborales)")
        console.print("[4] - Caja de Compensación")
        
        tipo_opc = console.input("\nSeleccione opción: ").strip()
        
        tipos = {
            "1": "EPS",
            "2": "Fondo de Pensiones",
            "3": "ARL",
            "4": "Caja de Compensación"
        }
        
        if tipo_opc not in tipos:
            console.print("[red]Opción inválida[/red]")
            console.input("Presione Enter para continuar...")
            return
        
        tipo_seleccionado = tipos[tipo_opc]
        
        # Buscar la afiliación de ese tipo
        afil_tipo = None
        for afil in afiliaciones:
            if afil[1] == candidato_id and afil[2] == tipo_seleccionado:
                afil_tipo = afil
                break
        
        if not afil_tipo:
            console.print(f"[yellow]No hay afiliación de {tipo_seleccionado} para este empleado[/yellow]")
            console.input("Presione Enter para continuar...")
            return
        
        # Mostrar datos actuales del tipo seleccionado
        console.print(Panel(
            f"Datos actuales de {tipo_seleccionado}:\n"
            f"Entidad: {afil_tipo[3]}\n"
            f"Número: {afil_tipo[4]}\n"
            f"Estado: {afil_tipo[6]}",
            title=tipo_seleccionado
        ))
        
        nueva_entidad = console.input("Nueva entidad (dejar vacío para mantener): ").strip()
        nuevo_numero = console.input("Nuevo número (dejar vacío para mantener): ").strip()
        
        # Actualizar con los nuevos valores
        ok = actualizar_afiliacion(
            afil_tipo[0],
            entidad=nueva_entidad if nueva_entidad else None,
            numero_afiliacion=nuevo_numero if nuevo_numero else None
        )
        
        if ok:
            set_status("Afiliación modificada")
            console.print(Panel(f"[green]✓ {tipo_seleccionado} modificada para {empleado_nombre}[/green]", style="green"))
        else:
            console.print(Panel("[red]Error al modificar[/red]", style="red"))
            
    except ValueError:
        console.print("[red]ID inválido[/red]")

    console.input("Presione Enter para continuar...")


def actualizar_una_afiliacion():
    """Actualizar estado de una afiliación"""
    clear_screen()
    console.rule("[bold cyan]Actualizar Estado de Afiliación")

    try:
        afil_id = int(console.input("Ingrese ID de la afiliación: ").strip())
        console.print("\nEstados disponibles:")
        console.print("1. Activa")
        console.print("2. Retirada")
        console.print("3. Pendiente")

        estado_num = int(console.input("\nSeleccione estado: ").strip())
        estados = {1: "Activa", 2: "Retirada", 3: "Pendiente"}

        if estado_num in estados:
            actualizar_estado_afiliacion(afil_id, estados[estado_num])
            set_status("Afiliación actualizada")
            console.print(
                Panel("[green]✓ Afiliación actualizada[/green]", style="green")
            )
        else:
            console.print("[red]Estado inválido[/red]")
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def eliminar_una_afiliacion():
    """Eliminar una afiliación"""
    clear_screen()
    console.rule("[bold cyan]Eliminar Afiliación")

    try:
        afil_id = int(console.input("Ingrese ID de la afiliación: ").strip())
        eliminar_afiliacion(afil_id)
        set_status("Afiliación eliminada")
        console.print(Panel("[green]✓ Afiliación eliminada[/green]", style="green"))
    except ValueError:
        console.print("[red]ID inválido[/red]")

    console.input("Presione Enter para continuar...")
