from services.Auth import authenticate


def prompt_login() -> bool:
    print("=== Login ===")
    usuario = input("Usuario: ").strip()
    password = input("Password: ").strip()
    ok = authenticate(usuario, password)
    if ok:
        print("Login exitoso\n")
    else:
        print("Credenciales inválidas\n")
    return ok
