from services.Candidatos import count_total, count_by_estado
from services.Contratos import count_total as contratos_total


def mostrar_reportes():
    print("=== Reportes ===")
    tot = count_total()
    estados = count_by_estado()
    ctot = contratos_total()
    print(f"Total candidatos: {tot}")
    print(f"Total contratos: {ctot}")
    print("Estados:")
    for k, v in estados.items():
        print(f"  {k}: {v}")
    print("")
