from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from services.Evaluaciones import (
    crear_evaluacion,
    obtener_todas_evaluaciones,
    obtener_evaluaciones_por_candidato,
    eliminar_evaluacion,
)
from services.Candidatos import obtener_todos_candidatos
from utils.ui import clear_screen
from utils.status import set_status

console = Console()


def gestionar_evaluaciones():
    """Menú principal de evaluaciones de desempeño"""
    while True:
        clear_screen()
        console.rule("[bold cyan]Evaluación de Desempeño")
        console.print(
            Panel(
                "[1] - Ver todas las evaluaciones\n"
                "[2] - Crear evaluación\n"
                "[3] - Ver evaluaciones por empleado\n"
                "[4] - Eliminar evaluación\n"
                "[5] - Volver",
                title="Opciones",
            )
        )
        opcion = console.input("Seleccione opción: ").strip()

        if opcion == "1":
            ver_todas_evaluaciones()
        elif opcion == "2":
            crear_nueva_evaluacion()
        elif opcion == "3":
            ver_evaluaciones_empleado()
        elif opcion == "4":
            eliminar_una_evaluacion()
        elif opcion == "5":
            break
        else:
            console.print("[red]Opción inválida[/red]")
            console.input("Presione Enter para continuar...")


def ver_todas_evaluaciones():
    """Ver todas las evaluaciones"""
    clear_screen()
    console.rule("[bold cyan]Todas las Evaluaciones")
    evaluaciones = obtener_todas_evaluaciones()

    if not evaluaciones:
        console.print("[yellow]No hay evaluaciones registradas[/yellow]")
        console.input("Presione Enter para continuar...")
        return

    table = Table(title="Evaluaciones de Desempeño")
    table.add_column("ID", style="cyan")
    table.add_column("Empleado", style="magenta")
    table.add_column("Fecha", style="green")
    table.add_column("Puntaje", style="yellow")
    table.add_column("Evaluador", style="blue")
    table.add_column("Estado", style="cyan")

    for eval in evaluaciones:
        table.add_row(
            str(eval[0]),
            eval[7],  # nombre
            str(eval[2]),
            f"{eval[3]}/100",
            str(eval[5]),
            eval[6],
        )

    console.print(table)
    console.input("Presione Enter para continuar...")


def crear_nueva_evaluacion():
    """Crear una nueva evaluación"""
    clear_screen()
    console.rule("[bold cyan]Crear Nueva Evaluación")

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
            puntaje = float(console.input("Puntaje (0-100): ").strip())
            if 0 <= puntaje <= 100:
                comentarios = console.input("Comentarios: ").strip()
                evaluador = console.input("Nombre del evaluador: ").strip()

                crear_evaluacion(candidato_id, puntaje, comentarios, evaluador)
                set_status("Evaluación creada exitosamente")
                console.print(
                    Panel("[green]✓ Evaluación creada[/green]", style="green")
                )
            else:
                console.print("[red]Puntaje debe estar entre 0 y 100[/red]")
        else:
            console.print("[red]Número inválido[/red]")
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def ver_evaluaciones_empleado():
    """Ver evaluaciones de un empleado"""
    clear_screen()
    console.rule("[bold cyan]Evaluaciones por Empleado")

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
            evaluaciones = obtener_evaluaciones_por_candidato(candidato_id)

            if not evaluaciones:
                console.print(
                    "[yellow]No hay evaluaciones para este empleado[/yellow]"
                )
            else:
                nombre_empleado = candidatos[num - 1]["nombre"]
                table = Table(
                    title=f"Evaluaciones de {nombre_empleado}"
                )
                table.add_column("ID", style="cyan")
                table.add_column("Fecha", style="green")
                table.add_column("Puntaje", style="yellow")
                table.add_column("Comentarios", style="blue")
                table.add_column("Evaluador", style="magenta")

                for eval in evaluaciones:
                    table.add_row(
                        str(eval[0]),
                        str(eval[2]),
                        f"{eval[3]}/100",
                        str(eval[4]),
                        str(eval[5]),
                    )

                console.print(table)
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def eliminar_una_evaluacion():
    """Eliminar una evaluación"""
    clear_screen()
    console.rule("[bold cyan]Eliminar Evaluación")

    try:
        eval_id = int(console.input("Ingrese ID de la evaluación: ").strip())
        eliminar_evaluacion(eval_id)
        set_status("Evaluación eliminada")
        console.print(Panel("[green]✓ Evaluación eliminada[/green]", style="green"))
    except ValueError:
        console.print("[red]ID inválido[/red]")

    console.input("Presione Enter para continuar...")
