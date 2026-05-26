from pathlib import Path
from services.Candidatos import count_total as total_candidatos, seed_10_candidatos
from services.Contratos import count_total as total_contratos, seed_4_contratos
from db.database import clear_business_data
from utils.ui import clear_screen
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()
MANUAL_PATH = Path(__file__).resolve().parents[1] / "README.md"


def show_manual():
    clear_screen()
    console.rule("[bold blue]Manual de Usuario")
    if not MANUAL_PATH.exists():
        console.print(Panel("No se encontró README.md.", style="red"))
        return
    content = MANUAL_PATH.read_text(encoding="utf-8")
    console.print(Markdown(content))


def developer_menu():
    while True:
        clear_screen()
        console.rule("[bold magenta]Desarrollador")
        menu = Panel.fit(
            "[b magenta]Acciones:[/b magenta]\n[magenta]1 - Limpiar BD[/magenta]\n[magenta]2 - Cargar Ejemplo[/magenta]\n[magenta]3 - Volver[/magenta]",
            title="Desarrollador",
            border_style="magenta",
        )
        console.print(menu)
        opc = console.input("Seleccione opción: ").strip()
        if opc == "1":
            clear_business_data()
            console.print(Panel("Base de datos limpiada: candidatos y contratos en 0.", style="magenta"))
        elif opc == "2":
            clear_business_data()
            n_candidatos = seed_10_candidatos()
            n_contratos = seed_4_contratos()
            console.print(
                Panel(
                    f"Ejemplo cargado: {n_candidatos} candidatos y {n_contratos} contratos.",
                    style="magenta",
                )
            )
        elif opc == "3":
            return
        else:
            console.print(Panel("Opción inválida", style="magenta"))


def show_dashboard():
    clear_screen()
    console.rule("[bold blue]Dashboard")
    t = Table(show_header=False, box=None)
    t.add_column("k", width=20)
    t.add_column("v")
    t.add_row("Total candidatos:", str(total_candidatos()))
    t.add_row("Total contratos:", str(total_contratos()))
    console.print(t)
    menu = Panel.fit(
        "[b]Opciones:[/b]\n1 - Gestionar candidatos\n2 - Generar contrato\n3 - Reportes\n4 - Desarrollador\n5 - Manual de usuario\n6 - Salir",
        title="Menú",
        border_style="green",
    )
    console.print(menu)
    return console.input("Seleccione opción: ").strip()
