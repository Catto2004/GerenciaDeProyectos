from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from services.Induccion import (
    crear_induccion,
    obtener_inducciones_por_candidato,
    obtener_todas_inducciones,
    actualizar_induccion,
    eliminar_induccion,
)
from services.Candidatos import obtener_todos_candidatos
from utils.ui import clear_screen
from utils.status import set_status

console = Console()


def gestionar_induccion():
    """Menú principal de inducción"""
    while True:
        clear_screen()
        console.rule("[bold cyan]Gestión de Inducción")
        console.print(
            Panel(
                "[1] - Ver todas las inducciones\n"
                "[2] - Registrar inducción\n"
                "[3] - Ver inducciones por empleado\n"
                "[4] - Actualizar inducción\n"
                "[5] - Eliminar inducción\n"
                "[6] - Volver",
                title="Opciones",
            )
        )
        opcion = console.input("Seleccione opción: ").strip()

        if opcion == "1":
            ver_todas_inducciones()
        elif opcion == "2":
            registrar_nueva_induccion()
        elif opcion == "3":
            ver_inducciones_empleado()
        elif opcion == "4":
            actualizar_una_induccion()
        elif opcion == "5":
            eliminar_una_induccion()
        elif opcion == "6":
            break
        else:
            console.print("[red]Opción inválida[/red]")
            console.input("Presione Enter para continuar...")


def ver_todas_inducciones():
    """Ver todas las inducciones"""
    clear_screen()
    console.rule("[bold cyan]Todas las Inducciones")
    inducciones = obtener_todas_inducciones()

    if not inducciones:
        console.print("[yellow]No hay inducciones registradas[/yellow]")
        console.input("Presione Enter para continuar...")
        return

    table = Table(title="Inducciones")
    table.add_column("ID", style="cyan")
    table.add_column("Empleado", style="magenta")
    table.add_column("Tipo", style="green")
    table.add_column("Fecha", style="yellow")
    table.add_column("Responsable", style="blue")
    table.add_column("Estado", style="cyan")

    for ind in inducciones:
        table.add_row(
            str(ind[0]),
            ind[7],  # nombre
            str(ind[2]),
            str(ind[3]),
            str(ind[4]),
            ind[6],
        )

    console.print(table)
    console.input("Presione Enter para continuar...")


def registrar_nueva_induccion():
    """Registrar una nueva inducción"""
    clear_screen()
    console.rule("[bold cyan]Registrar Nueva Inducción")

    candidatos = obtener_todos_candidatos()
    if not candidatos:
        console.print("[red]No hay empleados registrados[/red]")
        console.input("Presione Enter para continuar...")
        return

    console.print("\n[bold]Empleados disponibles:[/bold]")
    for i, cand in enumerate(candidatos, 1):
        console.print(f"{i}. {cand['nombre']}")

    try:
        num = int(console.input("\nSeleccione número de empleado: ").strip())
        if 1 <= num <= len(candidatos):
            candidato_id = candidatos[num - 1]["id"]

            console.print("\n[bold]Tipos de Inducción:[/bold]")
            console.print("1. Inducción Inicial")
            console.print("2. Re-inducción")
            console.print("3. Entrenamiento Específico")

            tipo_num = int(console.input("\nSeleccione tipo: ").strip())
            tipos = {
                1: "Inducción Inicial",
                2: "Re-inducción",
                3: "Entrenamiento Específico",
            }

            if tipo_num in tipos:
                tipo = tipos[tipo_num]
                responsable = console.input("Responsable de la inducción: ").strip()
                temas = console.input(
                    "Temas cubiertos (separados por coma): "
                ).strip()

                crear_induccion(candidato_id, tipo, responsable, temas)
                set_status("Inducción registrada exitosamente")
                console.print(
                    Panel("[green]✓ Inducción registrada[/green]", style="green")
                )
            else:
                console.print("[red]Tipo inválido[/red]")
        else:
            console.print("[red]Número inválido[/red]")
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def ver_inducciones_empleado():
    """Ver inducciones de un empleado"""
    clear_screen()
    console.rule("[bold cyan]Inducciones por Empleado")

    candidatos = obtener_todos_candidatos()
    if not candidatos:
        console.print("[red]No hay empleados registrados[/red]")
        console.input("Presione Enter para continuar...")
        return

    console.print("\n[bold]Empleados:[/bold]")
    for i, cand in enumerate(candidatos, 1):
        console.print(f"{i}. {cand['nombre']}")

    try:
        num = int(console.input("\nSeleccione número: ").strip())
        if 1 <= num <= len(candidatos):
            candidato_id = candidatos[num - 1]["id"]
            inducciones = obtener_inducciones_por_candidato(candidato_id)

            if not inducciones:
                console.print(
                    "[yellow]No hay inducciones para este empleado[/yellow]"
                )
            else:
                nombre_empleado = candidatos[num - 1]["nombre"]
                table = Table(
                    title=f"Inducciones de {nombre_empleado}"
                )
                table.add_column("ID", style="cyan")
                table.add_column("Tipo", style="green")
                table.add_column("Fecha", style="yellow")
                table.add_column("Responsable", style="blue")
                table.add_column("Temas", style="magenta")

                for ind in inducciones:
                    table.add_row(
                        str(ind[0]),
                        str(ind[2]),
                        str(ind[3]),
                        str(ind[4]),
                        str(ind[5]),
                    )

                console.print(table)
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def actualizar_una_induccion():
    """Actualizar información de una inducción"""
    clear_screen()
    console.rule("[bold cyan]Actualizar Inducción")

    try:
        induccion_id = int(console.input("Ingrese ID de la inducción: ").strip())
        temas = console.input("Nuevos temas cubiertos: ").strip()
        responsable = console.input("Nuevo responsable: ").strip()

        actualizar_induccion(induccion_id, temas, responsable)
        set_status("Inducción actualizada")
        console.print(
            Panel("[green]✓ Inducción actualizada[/green]", style="green")
        )
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def eliminar_una_induccion():
    """Eliminar una inducción"""
    clear_screen()
    console.rule("[bold cyan]Eliminar Inducción")

    try:
        induccion_id = int(console.input("Ingrese ID de la inducción: ").strip())
        eliminar_induccion(induccion_id)
        set_status("Inducción eliminada")
        console.print(Panel("[green]✓ Inducción eliminada[/green]", style="green"))
    except ValueError:
        console.print("[red]ID inválido[/red]")

    console.input("Presione Enter para continuar...")
