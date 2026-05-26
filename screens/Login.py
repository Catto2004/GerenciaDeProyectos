from services.Auth import authenticate
from rich.console import Console
from rich.panel import Panel
from getpass import getpass
from utils.ui import clear_screen

console = Console()


def prompt_login() -> bool:
    clear_screen()
    console.rule("[bold blue]Login")
    usuario = console.input("Usuario: ").strip()
    password = getpass("Password: ")
    ok = authenticate(usuario, password)
    if ok:
        console.print(Panel("Login exitoso", style="green"))
    else:
        console.print(Panel("Credenciales inválidas", style="red"))
    return ok
