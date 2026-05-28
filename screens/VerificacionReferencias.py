"""Pantalla de Verificación de Referencias."""
from services.VerificacionReferencias import (
    crear_verificacion,
    obtener_todas_verificaciones,
    obtener_verificaciones_por_candidato,
    eliminar_verificacion,
)
from services.Candidatos import list_candidatos
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from utils.ui import clear_screen, pause
from utils.status import render_status_panel, set_status

console = Console()


def gestionar_verificaciones():
    """Menú principal de verificación de referencias"""
    while True:
        clear_screen()
        console.rule("[bold blue]Verificación de Referencias")
        console.print(render_status_panel())
        menu = Panel.fit(
            "[b]Opciones:[/b]\n"
            "1 - Ver todas las verificaciones\n"
            "2 - Registrar verificación\n"
            "3 - Ver por candidato\n"
            "4 - Eliminar verificación\n"
            "5 - Volver",
            title="Referencias",
            border_style="green",
        )
        console.print(menu)
        opcion = console.input("Seleccione opción: ").strip()

        if opcion == "1":
            ver_todas_verificaciones()
        elif opcion == "2":
            registrar_nueva_verificacion()
        elif opcion == "3":
            ver_verificaciones_candidato()
        elif opcion == "4":
            eliminar_una_verificacion()
        elif opcion == "5":
            break
        else:
            console.print("[red]Opción inválida[/red]")
            pause()


def ver_todas_verificaciones():
    """Ver todas las verificaciones"""
    clear_screen()
    console.rule("[bold cyan]Todas las Verificaciones")
    verificaciones = obtener_todas_verificaciones()

    if not verificaciones:
        console.print("[yellow]No hay verificaciones registradas[/yellow]")
        pause()
        return

    table = Table(title="Verificación de Referencias")
    table.add_column("ID", style="cyan")
    table.add_column("Candidato", style="green")
    table.add_column("Referencia", style="yellow")
    table.add_column("Empresa", style="magenta")
    table.add_column("Verificada", style="blue")
    table.add_column("Fecha", style="white")

    for v in verificaciones:
        table.add_row(
            str(v[0]),
            v[11] if len(v) > 11 else "",
            v[2],
            v[4],
            v[7],
            v[9]
        )

    console.print(table)
    pause()


def registrar_nueva_verificacion():
    """Registrar una nueva verificación"""
    clear_screen()
    candidatos = list_candidatos()

    if not candidatos:
        console.print("[red]No hay candidatos[/red]")
        pause()
        return

    console.print("\n[bold]Seleccione candidato:[/bold]")
    for i, c in enumerate(candidatos, 1):
        console.print(f"{i}. {c[1]}")

    try:
        num = int(console.input("\nNúmero: ").strip())
        if 1 <= num <= len(candidatos):
            candidato_id = candidatos[num - 1][0]
            
            nombre_ref = console.input("Nombre de referencia: ").strip()
            telefono = console.input("Teléfono: ").strip()
            empresa = console.input("Empresa: ").strip()
            cargo = console.input("Cargo: ").strip()
            
            console.print("\n[bold]Relación:[/bold]")
            console.print("1. Jefe directo")
            console.print("2. Compañero")
            console.print("3. Subordinado")
            console.print("4. Cliente")
            rel = console.input("Seleccione: ").strip()
            relaciones = {"1": "Jefe directo", "2": "Compañero", "3": "Subordinado", "4": "Cliente"}
            
            console.print("\n[bold]Resultado:[/bold]")
            console.print("1. Positiva")
            console.print("2. Negativa")
            console.print("3. Neutral")
            res = console.input("Seleccione: ").strip()
            resultados = {"1": "Positiva", "2": "Negativa", "3": "Neutral"}
            
            observaciones = console.input("Observaciones: ").strip()
            
            crear_verificacion(candidato_id, nombre_ref, telefono, empresa, cargo, 
                           relaciones.get(rel, "Jefe directo"), resultados.get(res, "Neutral"), 
                           observaciones)
            set_status("Verificación registrada")
    except ValueError:
        console.print("[red]Entrada inválida[/red]")
    
    pause()


def ver_verificaciones_candidato():
    """Ver verificaciones de un candidato"""
    clear_screen()
    candidatos = list_candidatos()

    if not candidatos:
        console.print("[red]No hay candidatos[/red]")
        pause()
        return

    console.print("\n[bold]Seleccione candidato:[/bold]")
    for i, c in enumerate(candidatos, 1):
        console.print(f"{i}. {c[1]}")

    try:
        num = int(console.input("\nNúmero: ").strip())
        if 1 <= num <= len(candidatos):
            candidato_id = candidatos[num - 1][0]
            verificaciones = obtener_verificaciones_por_candidato(candidato_id)

            if not verificaciones:
                console.print("[yellow]No hay verificaciones[/yellow]")
            else:
                table = Table(title=f"Referencias: {candidatos[num-1][1]}")
                table.add_column("ID", style="cyan")
                table.add_column("Referencia", style="yellow")
                table.add_column("Empresa", style="magenta")
                table.add_column("Verificada", style="blue")

                for v in verificaciones:
                    table.add_row(str(v[0]), v[2], v[4], v[7])
                
                console.print(table)
    except ValueError:
        console.print("[red]Entrada inválida[/red]")
    
    pause()


def eliminar_una_verificacion():
    """Eliminar una verificación"""
    clear_screen()
    try:
        verif_id = int(console.input("ID de verificación a eliminar: ").strip())
        eliminar_verificacion(verif_id)
        set_status("Verificación eliminada")
    except ValueError:
        console.print("[red]ID inválido[/red]")
    
    pause()
