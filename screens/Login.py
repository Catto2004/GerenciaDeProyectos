from services.Auth import authenticate
from rich.console import Console
from rich.panel import Panel
from utils.ui import clear_screen
from utils.status import render_status_panel, set_status

console = Console()


def prompt_login() -> bool:
    clear_screen()
    console.rule("[bold blue]Login")
    console.print(render_status_panel())
    usuario = console.input("Usuario: ").strip()
    password = console.input("Password: ", password=True)
    ok = authenticate(usuario, password)
    if ok:
        set_status(f"Login exitoso para {usuario}")
        console.print(Panel("Login exitoso", style="green"))
    else:
        set_status("Intento de login fallido")
        console.print(Panel("Credenciales inválidas", style="red"))
    return ok
