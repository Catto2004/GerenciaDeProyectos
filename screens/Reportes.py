from services.Candidatos import count_total, count_by_estado, list_candidatos
from services.Contratos import count_total as contratos_total
from services.Contratos import list_contratados
from utils.ui import clear_screen, pause
from utils.status import render_status_panel, set_status
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def mostrar_reportes():
    clear_screen()
    console.rule("[bold blue]Reportes")
    console.print(render_status_panel())
    tot = count_total()
    estados = count_by_estado()
    ctot = contratos_total()
    t = Table(show_header=False, box=None)
    t.add_column("k", width=20)
    t.add_column("v")
    t.add_row("Total candidatos:", str(tot))
    t.add_row("Total contratos:", str(ctot))
    console.print(t)
    if estados:
        est_table = Table(title="Estados")
        est_table.add_column("Estado")
        est_table.add_column("Cantidad", justify="right")
        for k, v in estados.items():
            est_table.add_row(k, str(v))
        console.print(est_table)
    candidatos = list_candidatos()
    if candidatos:
        cand_table = Table(title="Candidatos")
        cand_table.add_column("ID", style="cyan", width=6)
        cand_table.add_column("Nombre", style="magenta")
        cand_table.add_column("Correo", style="green")
        cand_table.add_column("Teléfono", style="yellow")
        cand_table.add_column("Estado", style="red")
        for candidato in candidatos:
            cand_table.add_row(
                str(candidato["id"]),
                candidato["nombre"],
                candidato["correo"],
                candidato["telefono"],
                candidato["estado"],
            )
        console.print(cand_table)
    contratados = list_contratados()
    if contratados:
        table = Table(title="Contratados")
        table.add_column("ID", style="cyan", width=6)
        table.add_column("Nombre", style="magenta")
        table.add_column("Tipo", style="green")
        table.add_column("Fecha", style="yellow")
        for c in contratados:
            table.add_row(str(c["id"]), c["nombre"], c["tipo"], str(c["fecha"]))
        console.print(table)
        set_status(f"Reporte mostrado con {len(contratados)} contratados")
    console.print(Panel("Fin de reporte", style="blue"))
    pause()
