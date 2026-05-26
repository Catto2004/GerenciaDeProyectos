import os


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def pause(message: str = "Presiona Enter para continuar...") -> None:
    input(message)
