from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from services.Capacitaciones import (
    crear_capacitacion,
    obtener_todas_capacitaciones,
    registrar_asistencia,
    obtener_asistencia_por_capacitacion,
    actualizar_estado_capacitacion,
)
from services.Candidatos import obtener_todos_candidatos
from utils.ui import clear_screen
from utils.status import set_status

console = Console()


def gestionar_capacitaciones():
    """Menú principal de capacitaciones"""
    while True:
        clear_screen()
        console.rule("[bold cyan]Gestión de Capacitaciones")
        console.print(
            Panel(
                "[1] - Ver todas las capacitaciones\n"
                "[2] - Crear capacitación\n"
                "[3] - Registrar asistencia\n"
                "[4] - Ver asistencia por capacitación\n"
                "[5] - Cambiar estado\n"
                "[6] - Volver",
                title="Opciones",
            )
        )
        opcion = console.input("Seleccione opción: ").strip()

        if opcion == "1":
            ver_todas_capacitaciones()
        elif opcion == "2":
            crear_nueva_capacitacion()
        elif opcion == "3":
            registrar_nueva_asistencia()
        elif opcion == "4":
            ver_asistencia()
        elif opcion == "5":
            cambiar_estado_capacitacion()
        elif opcion == "6":
            break
        else:
            console.print("[red]Opción inválida[/red]")
            console.input("Presione Enter para continuar...")


def ver_todas_capacitaciones():
    """Ver todas las capacitaciones"""
    clear_screen()
    console.rule("[bold cyan]Todas las Capacitaciones")
    capacitaciones = obtener_todas_capacitaciones()

    if not capacitaciones:
        console.print("[yellow]No hay capacitaciones registradas[/yellow]")
        console.input("Presione Enter para continuar...")
        return

    table = Table(title="Capacitaciones")
    table.add_column("ID", style="cyan")
    table.add_column("Nombre", style="magenta")
    table.add_column("Inicio", style="green")
    table.add_column("Fin", style="yellow")
    table.add_column("Instructor", style="blue")
    table.add_column("Estado", style="cyan")

    for cap in capacitaciones:
        table.add_row(
            str(cap[0]),
            str(cap[1]),
            str(cap[3]),
            str(cap[4]),
            str(cap[5]),
            cap[6],
        )

    console.print(table)
    console.input("Presione Enter para continuar...")


def crear_nueva_capacitacion():
    """Crear una nueva capacitación"""
    clear_screen()
    console.rule("[bold cyan]Crear Nueva Capacitación")

    try:
        nombre = console.input("Nombre de la capacitación: ").strip()
        descripcion = console.input("Descripción: ").strip()
        fecha_inicio = console.input("Fecha de inicio (YYYY-MM-DD): ").strip()
        fecha_fin = console.input("Fecha de fin (YYYY-MM-DD): ").strip()
        instructor = console.input("Instructor: ").strip()

        crear_capacitacion(nombre, descripcion, fecha_inicio, fecha_fin, instructor)
        set_status("Capacitación creada exitosamente")
        console.print(
            Panel("[green]✓ Capacitación creada[/green]", style="green")
        )
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def registrar_nueva_asistencia():
    """Registrar asistencia a una capacitación"""
    clear_screen()
    console.rule("[bold cyan]Registrar Asistencia")

    capacitaciones = obtener_todas_capacitaciones()
    if not capacitaciones:
        console.print("[red]No hay capacitaciones disponibles[/red]")
        console.input("Presione Enter para continuar...")
        return

    console.print("\n[bold]Capacitaciones disponibles:[/bold]")
    for i, cap in enumerate(capacitaciones, 1):
        console.print(f"{i}. {cap[1]}")

    try:
        cap_num = int(console.input("\nSeleccione número de capacitación: ").strip())
        if 1 <= cap_num <= len(capacitaciones):
            capacitacion_id = capacitaciones[cap_num - 1][0]

            candidatos = obtener_todos_candidatos()
            if not candidatos:
                console.print("[red]No hay empleados registrados[/red]")
                console.input("Presione Enter para continuar...")
                return

            console.print("\n[bold]Empleados:[/bold]")
            for i, cand in enumerate(candidatos, 1):
                console.print(f"{i}. {cand['nombre']}")

            cand_num = int(console.input("\nSeleccione número de empleado: ").strip())
            if 1 <= cand_num <= len(candidatos):
                candidato_id = candidatos[cand_num - 1]["id"]
                asistio = console.input("¿Asistió? (Si/No): ").strip().lower()
                calificacion = (
                    float(console.input("Calificación (0-100): ").strip())
                    if asistio == "si"
                    else 0
                )

                registrar_asistencia(
                    capacitacion_id, candidato_id, asistio, calificacion
                )
                set_status("Asistencia registrada")
                console.print(
                    Panel("[green]✓ Asistencia registrada[/green]", style="green")
                )
            else:
                console.print("[red]Número inválido[/red]")
        else:
            console.print("[red]Número inválido[/red]")
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def ver_asistencia():
    """Ver asistencia a una capacitación"""
    clear_screen()
    console.rule("[bold cyan]Asistencia por Capacitación")

    capacitaciones = obtener_todas_capacitaciones()
    if not capacitaciones:
        console.print("[red]No hay capacitaciones registradas[/red]")
        console.input("Presione Enter para continuar...")
        return

    console.print("\n[bold]Capacitaciones:[/bold]")
    for i, cap in enumerate(capacitaciones, 1):
        console.print(f"{i}. {cap[1]}")

    try:
        num = int(console.input("\nSeleccione número: ").strip())
        if 1 <= num <= len(capacitaciones):
            capacitacion_id = capacitaciones[num - 1][0]
            asistencia = obtener_asistencia_por_capacitacion(capacitacion_id)

            if not asistencia:
                console.print(
                    "[yellow]No hay registros de asistencia[/yellow]"
                )
            else:
                table = Table(
                    title=f"Asistencia: {capacitaciones[num - 1][1]}"
                )
                table.add_column("ID", style="cyan")
                table.add_column("Empleado", style="magenta")
                table.add_column("Asistió", style="green")
                table.add_column("Calificación", style="yellow")

                for asist in asistencia:
                    table.add_row(
                        str(asist[0]),
                        str(asist[5]),  # nombre
                        str(asist[4]),
                        f"{asist[5]}/100" if asist[5] else "N/A",
                    )

                console.print(table)
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def cambiar_estado_capacitacion():
    """Cambiar estado de una capacitación"""
    clear_screen()
    console.rule("[bold cyan]Cambiar Estado de Capacitación")

    capacitaciones = obtener_todas_capacitaciones()
    if not capacitaciones:
        console.print("[red]No hay capacitaciones registradas[/red]")
        console.input("Presione Enter para continuar...")
        return

    console.print("\n[bold]Capacitaciones:[/bold]")
    for i, cap in enumerate(capacitaciones, 1):
        console.print(f"{i}. {cap[1]} - {cap[6]}")

    try:
        num = int(console.input("\nSeleccione número: ").strip())
        if 1 <= num <= len(capacitaciones):
            capacitacion_id = capacitaciones[num - 1][0]

            console.print("\nEstados disponibles:")
            console.print("1. Programada")
            console.print("2. En curso")
            console.print("3. Completada")
            console.print("4. Cancelada")

            estado_num = int(console.input("\nSeleccione estado: ").strip())
            estados = {
                1: "Programada",
                2: "En curso",
                3: "Completada",
                4: "Cancelada",
            }

            if estado_num in estados:
                actualizar_estado_capacitacion(capacitacion_id, estados[estado_num])
                set_status("Estado actualizado")
                console.print(
                    Panel("[green]✓ Estado actualizado[/green]", style="green")
                )
            else:
                console.print("[red]Estado inválido[/red]")
        else:
            console.print("[red]Número inválido[/red]")
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")
