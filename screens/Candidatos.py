from services.Candidatos import add_candidato, list_candidatos


def gestionar_candidatos():
    while True:
        print("=== Gestión de Candidatos ===")
        print("1 - Agregar candidato")
        print("2 - Listar candidatos")
        print("3 - Volver")
        opc = input("Seleccione opción: ").strip()
        if opc == "1":
            nombre = input("Nombre: ").strip()
            correo = input("Correo: ").strip()
            telefono = input("Teléfono: ").strip()
            cid = add_candidato(nombre, correo, telefono)
            print(f"Candidato creado con id {cid}\n")
        elif opc == "2":
            rows = list_candidatos()
            if not rows:
                print("No hay candidatos registrados.\n")
            else:
                for r in rows:
                    print(f"{r['id']}: {r['nombre']} - {r['correo']} - {r['telefono']} - {r['estado']}")
                print("")
        elif opc == "3":
            return
        else:
            print("Opción inválida\n")
