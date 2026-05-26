from services.Candidatos import list_candidatos
from services.Contratos import generar_contrato, despedir_empleado, list_contratos, list_contratados
from datetime import date
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from utils.ui import clear_screen, pause
from utils.status import render_status_panel, set_status

console = Console()


def gestionar_contratos():
    while True:
        clear_screen()
        console.rule("[bold blue]Gestión de Contratos")
        console.print(render_status_panel())
        menu = Panel.fit(
            "[b]Opciones:[/b]\n1 - Generar contrato\n2 - Despedir empleado\n3 - Listar empleados\n4 - Volver",
            title="Contratos",
            border_style="green",
        )
        console.print(menu)
        opc = console.input("Seleccione opción: ").strip()
        if opc == "1":
            candidatos = list_candidatos()
            if not candidatos:
                set_status("No hay candidatos disponibles para contratar")
                console.print(Panel("No hay candidatos disponibles.", style="yellow"))
                pause()
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
                set_status("Id inválido al generar contrato")
                console.print(Panel("Id inválido", style="red"))
                pause()
                continue
            tipo = console.input("Tipo de contrato (Temporal/Indefinido): ").strip() or "Temporal"
            fecha = date.today().isoformat()
            contrato_id = generar_contrato(cid, fecha, tipo)
            set_status(f"Contrato generado con id {contrato_id}")
            console.print(Panel(f"Contrato generado con id {contrato_id}", style="green"))
            pause()
        elif opc == "2":
            candidatos = list_candidatos()
            if not candidatos:
                set_status("No hay candidatos disponibles para despedir")
                console.print(Panel("No hay candidatos disponibles.", style="yellow"))
                pause()
                continue
            table = Table(title="Candidatos disponibles para despedir")
            table.add_column("ID", style="cyan", width=6)
            table.add_column("Nombre", style="magenta")
            table.add_column("Estado", style="green")
            for c in candidatos:
                table.add_row(str(c["id"]), c["nombre"], c["estado"])
            console.print(table)
            try:
                cid = int(console.input("Id de candidato a despedir: ").strip())
            except ValueError:
                set_status("Id inválido al despedir empleado")
                console.print(Panel("Id inválido", style="red"))
                pause()
                continue
            ok = despedir_empleado(cid)
            if ok:
                set_status(f"Candidato {cid} despedido")
                console.print(Panel(f"Candidato {cid} despedido.", style="green"))
            else:
                set_status("Candidato no encontrado")
                console.print(Panel("Candidato no encontrado.", style="red"))
            pause()
        elif opc == "3":
            empleados = list_contratados()
            if not empleados:
                set_status("No hay empleados contratados")
                console.print(Panel("No hay empleados contratados.", style="yellow"))
            else:
                table = Table(title="Empleados contratados")
                table.add_column("ID", style="cyan", width=6)
                table.add_column("Nombre", style="magenta")
                table.add_column("Tipo", style="green")
                table.add_column("Fecha", style="yellow")
                for empleado in empleados:
                    table.add_row(str(empleado["id"]), empleado["nombre"], empleado["tipo"], str(empleado["fecha"]))
                console.print(table)
                set_status(f"Listado de empleados mostrado: {len(empleados)} registros")
            pause()
        elif opc == "4":
            set_status("Regresando al dashboard")
            return
        else:
            set_status("Opción inválida en contratos")
            console.print(Panel("Opción inválida", style="red"))
            pause()
