# Proyecto de Gestión de Talento Humano por Innovatech Colombia.
from db.database import init_db
from screens.Login import prompt_login
from screens.Dashboard import show_dashboard
from screens.Candidatos import gestionar_candidatos
from screens.Contratos import gestionar_contratos
from screens.Reportes import mostrar_reportes


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
			print("Saliendo. Hasta luego.")
			break
		else:
			print("Opción inválida\n")


if __name__ == "__main__":
	main()

