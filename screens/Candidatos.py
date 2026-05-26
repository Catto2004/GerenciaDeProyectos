from services.Candidatos import add_candidato, list_candidatos, delete_candidato
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from utils.ui import clear_screen, pause
from utils.status import render_status_panel, set_status

console = Console()


def gestionar_candidatos():
    while True:
        clear_screen()
        console.rule("[bold blue]Gestión de Candidatos")
        console.print(render_status_panel())
        menu = Panel.fit(
            "[b]Opciones:[/b]\n1 - Agregar candidato\n2 - Listar candidatos\n3 - Eliminar candidato\n4 - Volver",
            title="Candidatos",
            border_style="green",
        )
        console.print(menu)
        opc = console.input("Seleccione opción: ").strip()
        if opc == "1":
            nombre = console.input("Nombre: ").strip()
            correo = console.input("Correo: ").strip()
            telefono = console.input("Teléfono: ").strip()
            cid = add_candidato(nombre, correo, telefono)
            set_status(f"Candidato creado con id {cid}")
            console.print(Panel(f"Candidato creado con id {cid}", style="green"))
        elif opc == "2":
            rows = list_candidatos()
            if not rows:
                console.print(Panel("No hay candidatos registrados.", style="yellow"))
                pause()
            else:
                table = Table(title="Candidatos registrados")
                table.add_column("ID", style="cyan", width=6)
                table.add_column("Nombre", style="magenta")
                table.add_column("Correo", style="green")
                table.add_column("Teléfono", style="yellow")
                table.add_column("Estado", style="red")
                for r in rows:
                    table.add_row(str(r["id"]), r["nombre"], r["correo"], r["telefono"], r["estado"])
                console.print(table)
                set_status(f"Listado de candidatos mostrado: {len(rows)} registros")
                pause()
        elif opc == "3":
            rows = list_candidatos()
            if rows:
                table = Table(title="Candidatos disponibles para eliminar")
                table.add_column("ID", style="cyan", width=6)
                table.add_column("Nombre", style="magenta")
                table.add_column("Correo", style="green")
                table.add_column("Teléfono", style="yellow")
                table.add_column("Estado", style="red")
                for r in rows:
                    table.add_row(str(r["id"]), r["nombre"], r["correo"], r["telefono"], r["estado"])
                console.print(table)
            else:
                console.print(Panel("No hay candidatos registrados.", style="yellow"))
                pause()
                continue
            try:
                cid = int(console.input("Id de candidato a eliminar: ").strip())
            except ValueError:
                set_status("Id inválido al eliminar candidato")
                console.print(Panel("Id inválido", style="red"))
                pause()
                continue
            ok = delete_candidato(cid)
            if ok:
                set_status(f"Candidato {cid} eliminado")
                console.print(Panel(f"Candidato {cid} eliminado.", style="green"))
            else:
                set_status("Candidato no encontrado")
                console.print(Panel("Candidato no encontrado.", style="red"))
            pause()
        elif opc == "4":
            set_status("Regresando al dashboard")
            return
        else:
            set_status("Opción inválida en candidatos")
            console.print(Panel("Opción inválida", style="red"))
            pause()
