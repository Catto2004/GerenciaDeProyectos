"""Pantalla de Certificaciones Laborales."""
from services.Certificaciones import (
    crear_certificacion,
    obtener_todas_certificaciones,
    obtener_certificaciones_por_candidato,
    actualizar_estado_certificacion,
    eliminar_certificacion,
)
from services.Candidatos import list_candidatos
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from utils.ui import clear_screen, pause
from utils.status import render_status_panel, set_status

console = Console()


def gestionar_certificaciones():
    """Menú principal de certificaciones laborales"""
    while True:
        clear_screen()
        console.rule("[bold blue]Certificaciones Laborales")
        console.print(render_status_panel())
        menu = Panel.fit(
            "[b]Opciones:[/b]\n"
            "1 - Ver todas las certificaciones\n"
            "2 - Crear certificación\n"
            "3 - Ver certificaciones por empleado\n"
            "4 - Actualizar estado\n"
            "5 - Eliminar certificación\n"
            "6 - Volver",
            title="Certificaciones",
            border_style="green",
        )
        console.print(menu)
        opcion = console.input("Seleccione opción: ").strip()

        if opcion == "1":
            ver_todas_certificaciones()
        elif opcion == "2":
            crear_nueva_certificacion()
        elif opcion == "3":
            ver_certificaciones_empleado()
        elif opcion == "4":
            actualizar_estado()
        elif opcion == "5":
            eliminar_una_certificacion()
        elif opcion == "6":
            break
        else:
            console.print("[red]Opción inválida[/red]")
            pause()


def ver_todas_certificaciones():
    """Ver todas las certificaciones"""
    clear_screen()
    console.rule("[bold cyan]Todas las Certificaciones")
    certificaciones = obtener_todas_certificaciones()

    if not certificaciones:
        console.print("[yellow]No hay certificaciones registradas[/yellow]")
        pause()
        return

    table = Table(title="Certificaciones Laborales")
    table.add_column("ID", style="cyan")
    table.add_column("Empleado", style="green")
    table.add_column("Tipo", style="yellow")
    table.add_column("Fecha Solicitud", style="magenta")
    table.add_column("Estado", style="blue")

    for cert in certificaciones:
        table.add_row(
            str(cert[0]),
            cert[7] if len(cert) > 7 else "",
            cert[2],
            cert[3],
            cert[6]
        )

    console.print(table)
    pause()


def crear_nueva_certificacion():
    """Crear una nueva certificación"""
    clear_screen()
    candidatos = list_candidatos()

    if not candidatos:
        console.print("[red]No hay candidatos disponibles[/red]")
        pause()
        return

    console.print("\n[bold]Seleccione candidato:[/bold]")
    for i, c in enumerate(candidatos, 1):
        console.print(f"{i}. {c[1]}")

    try:
        num = int(console.input("\nNúmero: ").strip())
        if 1 <= num <= len(candidatos):
            candidato_id = candidatos[num - 1][0]
            
            console.print("\n[bold]Tipos de certificación:[/bold]")
            console.print("1. Laboral")
            console.print("2. Ingresos")
            console.print("3. Funciones")
            tipo = console.input("Seleccione tipo: ").strip()
            tipos = {"1": "Laboral", "2": "Ingresos", "3": "Funciones"}
            tipo_cert = tipos.get(tipo, "Laboral")
            
            contenido = console.input("Contenido: ").strip()
            
            crear_certificacion(candidato_id, tipo_cert, contenido)
            set_status("Certificación creada exitosamente")
    except ValueError:
        console.print("[red]Entrada inválida[/red]")
    
    pause()


def ver_certificaciones_empleado():
    """Ver certificaciones de un empleado"""
    clear_screen()
    candidatos = list_candidatos()

    if not candidatos:
        console.print("[red]No hay candidatos[/red]")
        pause()
        return

    console.print("\n[bold]Seleccione empleado:[/bold]")
    for i, c in enumerate(candidatos, 1):
        console.print(f"{i}. {c[1]}")

    try:
        num = int(console.input("\nNúmero: ").strip())
        if 1 <= num <= len(candidatos):
            candidato_id = candidatos[num - 1][0]
            certificaciones = obtener_certificaciones_por_candidato(candidato_id)

            if not certificaciones:
                console.print("[yellow]No hay certificaciones[/yellow]")
            else:
                table = Table(title=f"Certificaciones: {candidatos[num-1][1]}")
                table.add_column("ID", style="cyan")
                table.add_column("Tipo", style="yellow")
                table.add_column("Fecha", style="magenta")
                table.add_column("Estado", style="blue")

                for cert in certificaciones:
                    table.add_row(str(cert[0]), cert[2], cert[3], cert[6])
                
                console.print(table)
    except ValueError:
        console.print("[red]Entrada inválida[/red]")
    
    pause()


def actualizar_estado():
    """Actualizar estado de certificación"""
    clear_screen()
    try:
        cert_id = int(console.input("ID de certificación: ").strip())
        
        console.print("\n[bold]Estados:[/bold]")
        console.print("1. Pendiente")
        console.print("2. Emitida")
        console.print("3. Cancelada")
        estado = console.input("Nuevo estado: ").strip()
        estados = {"1": "Pendiente", "2": "Emitida", "3": "Cancelada"}
        
        if estado in estados:
            actualizar_estado_certificacion(cert_id, estados[estado])
            set_status("Estado actualizado")
    except ValueError:
        console.print("[red]ID inválido[/red]")
    
    pause()


def eliminar_una_certificacion():
    """Eliminar una certificación"""
    clear_screen()
    try:
        cert_id = int(console.input("ID de certificación a eliminar: ").strip())
        eliminar_certificacion(cert_id)
        set_status("Certificación eliminada")
    except ValueError:
        console.print("[red]ID inválido[/red]")
    
    pause()
