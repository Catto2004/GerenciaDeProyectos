from rich.panel import Panel

_last_message = "Listo"


def set_status(message: str) -> None:
    global _last_message
    _last_message = message or "Listo"


def get_status() -> str:
    return _last_message


def render_status_panel() -> Panel:
    return Panel.fit(f"[bold]Estatus:[/bold]\n{_last_message}", border_style="cyan", title="Estado")
