# Proyecto de Gestión de Talento Humano por Innovatech Colombia.
from db.database import init_db
from screens.Login import prompt_login
from screens.Dashboard import show_dashboard
from screens.Dashboard import developer_menu
from screens.Dashboard import show_manual
from screens.Candidatos import gestionar_candidatos
from screens.Contratos import gestionar_contratos
from screens.Reportes import mostrar_reportes
from screens.Nomina import gestionar_nomina
from screens.Afiliaciones import gestionar_afiliaciones
from screens.Evaluaciones import gestionar_evaluaciones
from screens.Capacitaciones import gestionar_capacitaciones
from screens.Retiro import gestionar_retiro
from screens.Induccion import gestionar_induccion
from screens.Certificaciones import gestionar_certificaciones
from screens.PruebasPsicotecnicas import gestionar_pruebas
from screens.VerificacionReferencias import gestionar_verificaciones
from rich.console import Console
from rich.panel import Panel

console = Console()


def menu_recursos_humanos():
	"""Menú de Recursos Humanos"""
	while True:
		from utils.ui import clear_screen
		clear_screen()
		console.rule("[bold cyan]Gestión de Recursos Humanos")
		console.print(
			Panel(
				"[1] - Nómina y Liquidaciones\n"
				"[2] - Afiliaciones (Seguridad Social)\n"
				"[3] - Evaluaciones de Desempeño\n"
				"[4] - Capacitaciones\n"
				"[5] - Retiro de Personal\n"
				"[6] - Inducción\n"
				"[7] - Certificaciones Laborales\n"
				"[8] - Pruebas Psicotécnicas\n"
				"[9] - Verificación de Referencias\n"
				"[10] - Volver",
				title="Opciones RR.HH.",
			)
		)
		opc = console.input("Seleccione opción: ").strip()
		
		if opc == "1":
			gestionar_nomina()
		elif opc == "2":
			gestionar_afiliaciones()
		elif opc == "3":
			gestionar_evaluaciones()
		elif opc == "4":
			gestionar_capacitaciones()
		elif opc == "5":
			gestionar_retiro()
		elif opc == "6":
			gestionar_induccion()
		elif opc == "7":
			gestionar_certificaciones()
		elif opc == "8":
			gestionar_pruebas()
		elif opc == "9":
			gestionar_verificaciones()
		elif opc == "10":
			break
		else:
			console.print("[red]Opción inválida[/red]")
			console.input("Presione Enter para continuar...")


def main():
	init_db()
	print("GerenciaDeProyectos - Prototipo académico\n")
	# Login simple
	for _ in range(3):
		ok = prompt_login()
		if ok:
			break
	else:
		print("Demasiados intentos. Saliendo.")
		return

	while True:
		opc = show_dashboard()
		if opc == "1":
			gestionar_candidatos()
		elif opc == "2":
			gestionar_contratos()
		elif opc == "3":
			mostrar_reportes()
		elif opc == "4":
			menu_recursos_humanos()
		elif opc == "5":
			developer_menu()
		elif opc == "6":
			show_manual()
		elif opc == "7":
			print("Saliendo. Hasta luego.")
			break
		else:
			print("Opción inválida\n")


if __name__ == "__main__":
	main()
