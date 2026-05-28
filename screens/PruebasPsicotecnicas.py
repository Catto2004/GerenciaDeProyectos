"""Pantalla de Pruebas Psicotécnicas."""
from services.PruebasPsicotecnicas import (
    crear_prueba_psicotecnica,
    obtener_todas_pruebas,
    obtener_pruebas_por_candidato,
    eliminar_prueba,
)
from services.Candidatos import list_candidatos
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from utils.ui import clear_screen, pause
from utils.status import render_status_panel, set_status

console = Console()


def gestionar_pruebas():
    """Menú principal de pruebas psicotécnicas"""
    while True:
        clear_screen()
        console.rule("[bold blue]Pruebas Psicotécnicas")
        console.print(render_status_panel())
        menu = Panel.fit(
            "[b]Opciones:[/b]\n"
            "1 - Ver todas las pruebas\n"
            "2 - Registrar prueba\n"
            "3 - Ver pruebas por candidato\n"
            "4 - Eliminar prueba\n"
            "5 - Volver",
            title="Pruebas Psicotécnicas",
            border_style="green",
        )
        console.print(menu)
        opcion = console.input("Seleccione opción: ").strip()

        if opcion == "1":
            ver_todas_pruebas()
        elif opcion == "2":
            registrar_nueva_prueba()
        elif opcion == "3":
            ver_pruebas_candidato()
        elif opcion == "4":
            eliminar_una_prueba()
        elif opcion == "5":
            break
        else:
            console.print("[red]Opción inválida[/red]")
            pause()


def ver_todas_pruebas():
    """Ver todas las pruebas"""
    clear_screen()
    console.rule("[bold cyan]Todas las Pruebas Psicotécnicas")
    pruebas = obtener_todas_pruebas()

    if not pruebas:
        console.print("[yellow]No hay pruebas registradas[/yellow]")
        pause()
        return

    table = Table(title="Pruebas Psicotécnicas")
    table.add_column("ID", style="cyan")
    table.add_column("Candidato", style="green")
    table.add_column("Tipo", style="yellow")
    table.add_column("Fecha", style="magenta")
    table.add_column("Puntaje", style="blue")
    table.add_column("Resultado", style="red")

    for pr in pruebas:
        table.add_row(
            str(pr[0]),
            pr[8] if len(pr) > 8 else "",
            pr[2],
            pr[3],
            str(pr[5]) if pr[5] else "",
            pr[4]
        )

    console.print(table)
    pause()


def registrar_nueva_prueba():
    """Registrar una nueva prueba"""
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
            
            console.print("\n[bold]Tipos de prueba:[/bold]")
            console.print("1. Personalidad")
            console.print("2. Inteligencia")
            console.print("3. Aptitudinal")
            console.print("4. Domino")
            tipo = console.input("Seleccione tipo: ").strip()
            tipos = {"1": "Personalidad", "2": "Inteligencia", "3": "Aptitudinal", "4": "Domino"}
            tipo_prueba = tipos.get(tipo, "Personalidad")
            
            console.print("\n[bold]Resultados:[/bold]")
            console.print("1. Apto")
            console.print("2. Apto con recomendaciones")
            console.print("3. No apto")
            res = console.input("Resultado: ").strip()
            resultados = {"1": "Apto", "2": "Apto con recomendaciones", "3": "No apto"}
            resultado = resultados.get(res, "Apto")
            
            puntaje = float(console.input("Puntaje: ").strip())
            observaciones = console.input("Observaciones: ").strip()
            evaluador = console.input("Evaluador: ").strip()
            
            crear_prueba_psicotecnica(candidato_id, tipo_prueba, resultado, puntaje, observaciones, evaluador)
            set_status("Prueba registrada exitosamente")
    except ValueError:
        console.print("[red]Entrada inválida[/red]")
    
    pause()


def ver_pruebas_candidato():
    """Ver pruebas de un candidato"""
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
            pruebas = obtener_pruebas_por_candidato(candidato_id)

            if not pruebas:
                console.print("[yellow]No hay pruebas[/yellow]")
            else:
                table = Table(title=f"Pruebas: {candidatos[num-1][1]}")
                table.add_column("ID", style="cyan")
                table.add_column("Tipo", style="yellow")
                table.add_column("Fecha", style="magenta")
                table.add_column("Puntaje", style="blue")
                table.add_column("Resultado", style="red")

                for pr in pruebas:
                    table.add_row(str(pr[0]), pr[2], pr[3], str(pr[5]) if pr[5] else "", pr[4])
                
                console.print(table)
    except ValueError:
        console.print("[red]Entrada inválida[/red]")
    
    pause()


def eliminar_una_prueba():
    """Eliminar una prueba"""
    clear_screen()
    try:
        prueba_id = int(console.input("ID de prueba a eliminar: ").strip())
        eliminar_prueba(prueba_id)
        set_status("Prueba eliminada")
    except ValueError:
        console.print("[red]ID inválido[/red]")
    
    pause()
