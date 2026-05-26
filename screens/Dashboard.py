from services.Candidatos import count_total as total_candidatos
from services.Contratos import count_total as total_contratos


def show_dashboard():
    print("=== Dashboard ===")
    print(f"Total candidatos: {total_candidatos()}")
    print(f"Total contratos: {total_contratos()}")
    print("\nOpciones:")
    print("1 - Gestionar candidatos")
    print("2 - Generar contrato")
    print("3 - Reportes")
    print("4 - Salir")
    return input("Seleccione opción: ").strip()
