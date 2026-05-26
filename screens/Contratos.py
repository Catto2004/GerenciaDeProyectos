from services.Candidatos import list_candidatos
from services.Contratos import generar_contrato
from datetime import date


def gestionar_contratos():
    print("=== Generar Contrato ===")
    candidatos = list_candidatos()
    if not candidatos:
        print("No hay candidatos disponibles.\n")
        return
    for c in candidatos:
        print(f"{c['id']}: {c['nombre']} - {c['estado']}")
    try:
        cid = int(input("Seleccionar id de candidato: ").strip())
    except ValueError:
        print("Id inválido\n")
        return
    tipo = input("Tipo de contrato (Temporal/Indefinido): ").strip() or "Temporal"
    fecha = date.today().isoformat()
    contrato_id = generar_contrato(cid, fecha, tipo)
    print(f"Contrato generado con id {contrato_id}\n")
