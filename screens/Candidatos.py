from services.Candidatos import add_candidato, list_candidatos, delete_candidato
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from utils.ui import clear_screen

console = Console()


def gestionar_candidatos():
    while True:
        clear_screen()
        console.rule("[bold blue]Gestión de Candidatos")
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
            console.print(Panel(f"Candidato creado con id {cid}", style="green"))
        elif opc == "2":
            rows = list_candidatos()
            if not rows:
                console.print(Panel("No hay candidatos registrados.", style="yellow"))
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
        elif opc == "3":
            try:
                cid = int(console.input("Id de candidato a eliminar: ").strip())
            except ValueError:
                console.print(Panel("Id inválido", style="red"))
                continue
            ok = delete_candidato(cid)
            if ok:
                console.print(Panel(f"Candidato {cid} eliminado.", style="green"))
            else:
                console.print(Panel("Candidato no encontrado.", style="red"))
        elif opc == "4":
            return
        else:
            console.print(Panel("Opción inválida", style="red"))
