from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from services.Nomina import (
    crear_liquidacion_nomina,
    obtener_todas_nominas,
    obtener_nominas_por_candidato,
    eliminar_liquidacion_nomina,
)
from services.Candidatos import obtener_todos_candidatos
from services.Contratos import list_contratados
from utils.ui import clear_screen
from utils.status import set_status

console = Console()


def gestionar_nomina():
    """Menú principal de gestión de nómina"""
    while True:
        clear_screen()
        console.rule("[bold cyan]Gestión de Nómina")
        console.print(
            Panel(
                "[1] - Ver todas las liquidaciones\n"
                "[2] - Crear liquidación\n"
                "[3] - Ver liquidaciones por empleado\n"
                "[4] - Eliminar liquidación\n"
                "[5] - Volver",
                title="Opciones",
            )
        )
        opcion = console.input("Seleccione opción: ").strip()

        if opcion == "1":
            ver_todas_liquidaciones()
        elif opcion == "2":
            crear_nueva_liquidacion()
        elif opcion == "3":
            ver_liquidaciones_empleado()
        elif opcion == "4":
            eliminar_una_liquidacion()
        elif opcion == "5":
            break
        else:
            console.print("[red]Opción inválida[/red]")
            console.input("Presione Enter para continuar...")


def ver_todas_liquidaciones():
    """Ver todas las liquidaciones de nómina"""
    clear_screen()
    console.rule("[bold cyan]Todas las Liquidaciones de Nómina")
    nominas = obtener_todas_nominas()

    if not nominas:
        console.print("[yellow]No hay liquidaciones registradas[/yellow]")
        console.input("Presione Enter para continuar...")
        return

    table = Table(title="Liquidaciones de Nómina")
    table.add_column("ID", style="cyan")
    table.add_column("Empleado", style="magenta")
    table.add_column("Período", style="green")
    table.add_column("Salario Base", style="yellow")
    table.add_column("Descuentos", style="red")
    table.add_column("Bonificaciones", style="green")
    table.add_column("Total Líquido", style="blue")
    table.add_column("Estado", style="cyan")

    for nomina in nominas:
        table.add_row(
            str(nomina[0]),
            nomina[9],  # nombre del empleado
            str(nomina[2]),
            f"${nomina[3]:.2f}",
            f"${nomina[4]:.2f}",
            f"${nomina[5]:.2f}",
            f"${nomina[6]:.2f}",
            nomina[8],
        )

    console.print(table)
    console.input("Presione Enter para continuar...")


def crear_nueva_liquidacion():
    """Crear una nueva liquidación de nómina"""
    clear_screen()
    console.rule("[bold cyan]Crear Nueva Liquidación")

    # Solo mostrar empleados contratados
    candidatos = list_contratados()
    if not candidatos:
        console.print("[red]No hay empleados contratados[/red]")
        console.input("Presione Enter para continuar...")
        return

    console.print("\n[bold]Empleados contratados:[/bold]")
    for i, cand in enumerate(candidatos, 1):
        console.print(f"{i}. {cand['nombre']} - {cand['tipo']}")

    try:
        num = int(console.input("\nSeleccione número de empleado: ").strip())
        if 1 <= num <= len(candidatos):
            candidato_id = candidatos[num - 1]["id"]
            periodo = console.input("Período (ej: Septiembre 2026): ").strip()
            salario_base = float(console.input("Salario base: $").strip())
            descuentos = float(console.input("Descuentos: $").strip())
            bonificaciones = float(console.input("Bonificaciones: $").strip())

            crear_liquidacion_nomina(
                candidato_id, periodo, salario_base, descuentos, bonificaciones
            )
            set_status("Liquidación creada exitosamente")
            console.print(Panel("[green]✓ Liquidación creada[/green]", style="green"))
        else:
            console.print("[red]Número inválido[/red]")
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def ver_liquidaciones_empleado():
    """Ver liquidaciones de un empleado específico"""
    clear_screen()
    console.rule("[bold cyan]Liquidaciones por Empleado")

    # Solo mostrar empleados contratados
    candidatos = list_contratados()
    if not candidatos:
        console.print("[red]No hay empleados contratados[/red]")
        console.input("Presione Enter para continuar...")
        return

    console.print("\n[bold]Empleados contratados:[/bold]")
    for i, cand in enumerate(candidatos, 1):
        console.print(f"{i}. {cand['nombre']}")

    try:
        num = int(console.input("\nSeleccione número: ").strip())
        if 1 <= num <= len(candidatos):
            candidato_id = candidatos[num - 1]["id"]
            nominas = obtener_nominas_por_candidato(candidato_id)

            if not nominas:
                console.print(
                    "[yellow]No hay liquidaciones para este empleado[/yellow]"
                )
            else:
                nombre_empleado = candidatos[num - 1]["nombre"]
                table = Table(
                    title=f"Liquidaciones de {nombre_empleado}"
                )
                table.add_column("ID", style="cyan")
                table.add_column("Período", style="green")
                table.add_column("Salario Base", style="yellow")
                table.add_column("Total Líquido", style="blue")
                table.add_column("Estado", style="cyan")

                for nomina in nominas:
                    table.add_row(
                        str(nomina[0]),
                        str(nomina[2]),
                        f"${nomina[3]:.2f}",
                        f"${nomina[6]:.2f}",
                        nomina[8],
                    )

                console.print(table)
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def eliminar_una_liquidacion():
    """Eliminar una liquidación"""
    clear_screen()
    console.rule("[bold cyan]Eliminar Liquidación")

    try:
        nomina_id = int(
            console.input("Ingrese ID de la liquidación a eliminar: ").strip()
        )
        eliminar_liquidacion_nomina(nomina_id)
        set_status("Liquidación eliminada")
        console.print(Panel("[green]✓ Liquidación eliminada[/green]", style="green"))
    except ValueError:
        console.print("[red]ID inválido[/red]")

    console.input("Presione Enter para continuar...")
