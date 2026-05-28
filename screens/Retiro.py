from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from services.Retiro import (
    crear_retiro,
    obtener_retiros,
    obtener_retiros_por_candidato,
    actualizar_estado_retiro,
    eliminar_retiro,
)
from services.Candidatos import obtener_todos_candidatos
from utils.ui import clear_screen
from utils.status import set_status

console = Console()


def gestionar_retiro():
    """Menú principal de retiro de personal"""
    while True:
        clear_screen()
        console.rule("[bold cyan]Retiro de Personal")
        console.print(
            Panel(
                "[1] - Ver todos los retiros\n"
                "[2] - Registrar retiro\n"
                "[3] - Ver retiros por empleado\n"
                "[4] - Actualizar estado\n"
                "[5] - Eliminar retiro\n"
                "[6] - Volver",
                title="Opciones",
            )
        )
        opcion = console.input("Seleccione opción: ").strip()

        if opcion == "1":
            ver_todos_retiros()
        elif opcion == "2":
            registrar_nuevo_retiro()
        elif opcion == "3":
            ver_retiros_empleado()
        elif opcion == "4":
            actualizar_un_retiro()
        elif opcion == "5":
            eliminar_un_retiro()
        elif opcion == "6":
            break
        else:
            console.print("[red]Opción inválida[/red]")
            console.input("Presione Enter para continuar...")


def ver_todos_retiros():
    """Ver todos los retiros"""
    clear_screen()
    console.rule("[bold cyan]Todos los Retiros")
    retiros = obtener_retiros()

    if not retiros:
        console.print("[yellow]No hay retiros registrados[/yellow]")
        console.input("Presione Enter para continuar...")
        return

    table = Table(title="Retiros de Personal")
    table.add_column("ID", style="cyan")
    table.add_column("Empleado", style="magenta")
    table.add_column("Fecha Retiro", style="green")
    table.add_column("Motivo", style="yellow")
    table.add_column("Liquidación", style="blue")
    table.add_column("Estado", style="cyan")

    for ret in retiros:
        table.add_row(
            str(ret[0]),
            ret[7],  # nombre
            str(ret[2]),
            str(ret[3]),
            f"${ret[4]:.2f}",
            ret[5],
        )

    console.print(table)
    console.input("Presione Enter para continuar...")


def registrar_nuevo_retiro():
    """Registrar un nuevo retiro de personal"""
    clear_screen()
    console.rule("[bold cyan]Registrar Retiro de Personal")

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

            console.print("\n[bold]Motivos de retiro:[/bold]")
            console.print("1. Renuncia")
            console.print("2. Despido")
            console.print("3. Finalización de contrato")
            console.print("4. Jubilación")
            console.print("5. Otro")

            motivo_num = int(console.input("\nSeleccione motivo: ").strip())
            motivos = {
                1: "Renuncia",
                2: "Despido",
                3: "Finalización de contrato",
                4: "Jubilación",
                5: "Otro",
            }

            if motivo_num in motivos:
                motivo = motivos[motivo_num]
                if motivo_num == 5:
                    motivo = console.input("Especifique el motivo: ").strip()

                liquidacion = float(console.input("Liquidación total ($): ").strip())

                crear_retiro(candidato_id, motivo, liquidacion)
                set_status("Retiro registrado exitosamente")
                console.print(
                    Panel("[green]✓ Retiro registrado[/green]", style="green")
                )
            else:
                console.print("[red]Motivo inválido[/red]")
        else:
            console.print("[red]Número inválido[/red]")
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def ver_retiros_empleado():
    """Ver retiros de un empleado específico"""
    clear_screen()
    console.rule("[bold cyan]Retiros por Empleado")

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
            retiros = obtener_retiros_por_candidato(candidato_id)

            if not retiros:
                console.print("[yellow]No hay retiros para este empleado[/yellow]")
            else:
                nombre_empleado = candidatos[num - 1]["nombre"]
                table = Table(title=f"Retiros de {nombre_empleado}")
                table.add_column("ID", style="cyan")
                table.add_column("Fecha", style="green")
                table.add_column("Motivo", style="yellow")
                table.add_column("Liquidación", style="blue")
                table.add_column("Estado", style="cyan")

                for ret in retiros:
                    table.add_row(
                        str(ret[0]),
                        str(ret[2]),
                        str(ret[3]),
                        f"${ret[4]:.2f}",
                        ret[5],
                    )

                console.print(table)
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def actualizar_un_retiro():
    """Actualizar estado de un retiro"""
    clear_screen()
    console.rule("[bold cyan]Actualizar Estado de Retiro")

    try:
        retiro_id = int(console.input("Ingrese ID del retiro: ").strip())

        console.print("\n[bold]Estados disponibles:[/bold]")
        console.print("1. Pendiente")
        console.print("2. Procesando")
        console.print("3. Completado")
        console.print("4. Cancelado")

        estado_num = int(console.input("\nSeleccione estado: ").strip())
        estados = {
            1: "Pendiente",
            2: "Procesando",
            3: "Completado",
            4: "Cancelado",
        }

        if estado_num in estados:
            actualizar_estado_retiro(retiro_id, estados[estado_num])
            set_status("Retiro actualizado")
            console.print(
                Panel("[green]✓ Retiro actualizado[/green]", style="green")
            )
        else:
            console.print("[red]Estado inválido[/red]")
    except ValueError:
        console.print("[red]Error en los datos ingresados[/red]")

    console.input("Presione Enter para continuar...")


def eliminar_un_retiro():
    """Eliminar un retiro"""
    clear_screen()
    console.rule("[bold cyan]Eliminar Retiro")

    try:
        retiro_id = int(console.input("Ingrese ID del retiro a eliminar: ").strip())
        eliminar_retiro(retiro_id)
        set_status("Retiro eliminado")
        console.print(Panel("[green]✓ Retiro eliminado[/green]", style="green"))
    except ValueError:
        console.print("[red]ID inválido[/red]")

    console.input("Presione Enter para continuar...")
