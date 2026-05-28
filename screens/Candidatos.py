from services.Candidatos import add_candidato, list_candidatos, delete_candidato, update_candidato, get_candidato_by_id
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
            "[b]Opciones:[/b]\n1 - Agregar candidato\n2 - Listar candidatos\n3 - Editar candidato\n4 - Eliminar candidato\n5 - Volver",
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
            # Editar candidato
            rows = list_candidatos()
            if rows:
                table = Table(title="Candidatos disponibles para editar")
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
                cid = int(console.input("Id de candidato a editar: ").strip())
            except ValueError:
                set_status("Id inválido al editar candidato")
                console.print(Panel("Id inválido", style="red"))
                pause()
                continue
            candidato = get_candidato_by_id(cid)
            if not candidato:
                set_status("Candidato no encontrado")
                console.print(Panel("Candidato no encontrado.", style="red"))
                pause()
                continue
            # Mostrar datos actuales y pedir nuevos valores
            console.print(Panel(f"Datos actuales:\nNombre: {candidato['nombre']}\nCorreo: {candidato['correo']}\nTeléfono: {candidato['telefono']}\nEstado: {candidato['estado']}", title=f"Editar candidato {cid}"))
            nuevo_nombre = console.input(f"Nuevo nombre (actual: {candidato['nombre']}): ").strip()
            nuevo_correo = console.input(f"Nuevo correo (actual: {candidato['correo']}): ").strip()
            nuevo_telefono = console.input(f"Nuevo teléfono (actual: {candidato['telefono']}): ").strip()
            nuevo_estado = console.input(f"Nuevo estado (actual: {candidato['estado']}): ").strip()
            
            # Update if fields are not empty
            ok = update_candidato(
                cid,
                nombre=nuevo_nombre if nuevo_nombre else None,
                correo=nuevo_correo if nuevo_correo else None,
                telefono=nuevo_telefono if nuevo_telefono else None,
                estado=nuevo_estado if nuevo_estado else None
            )
            if ok:
                set_status(f"Candidato {cid} actualizado")
                console.print(Panel(f"Candidato {cid} actualizado.", style="green"))
            else:
                set_status("Error al actualizar candidato")
                console.print(Panel("Error al actualizar candidato.", style="red"))
            pause()
        elif opc == "4":
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
        elif opc == "5":
            set_status("Regresando al dashboard")
            return
        else:
            set_status("Opción inválida en candidatos")
            console.print(Panel("Opción inválida", style="red"))
            pause()
