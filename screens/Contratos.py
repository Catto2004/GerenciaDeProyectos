from services.Candidatos import list_candidatos
from services.Contratos import generar_contrato, despedir_empleado
from datetime import date
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from utils.ui import clear_screen

console = Console()


def gestionar_contratos():
    while True:
        clear_screen()
        console.rule("[bold blue]Gestión de Contratos")
        menu = Panel.fit(
            "[b]Opciones:[/b]\n1 - Generar contrato\n2 - Despedir empleado\n3 - Volver",
            title="Contratos",
            border_style="green",
        )
        console.print(menu)
        opc = console.input("Seleccione opción: ").strip()
        if opc == "1":
            candidatos = list_candidatos()
            if not candidatos:
                console.print(Panel("No hay candidatos disponibles.", style="yellow"))
                continue
            table = Table(title="Candidatos")
            table.add_column("ID", style="cyan", width=6)
            table.add_column("Nombre", style="magenta")
            table.add_column("Estado", style="green")
            for c in candidatos:
                table.add_row(str(c["id"]), c["nombre"], c["estado"])
            console.print(table)
            try:
                cid = int(console.input("Seleccionar id de candidato: ").strip())
            except ValueError:
                console.print(Panel("Id inválido", style="red"))
                continue
            tipo = console.input("Tipo de contrato (Temporal/Indefinido): ").strip() or "Temporal"
            fecha = date.today().isoformat()
            contrato_id = generar_contrato(cid, fecha, tipo)
            console.print(Panel(f"Contrato generado con id {contrato_id}", style="green"))
        elif opc == "2":
            try:
                cid = int(console.input("Id de candidato a despedir: ").strip())
            except ValueError:
                console.print(Panel("Id inválido", style="red"))
                continue
            ok = despedir_empleado(cid)
            if ok:
                console.print(Panel(f"Candidato {cid} despedido.", style="green"))
            else:
                console.print(Panel("Candidato no encontrado.", style="red"))
        elif opc == "3":
            return
        else:
            console.print(Panel("Opción inválida", style="red"))
