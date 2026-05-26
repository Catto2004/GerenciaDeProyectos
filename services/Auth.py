from db.database import get_connection


def authenticate(usuario: str, password: str) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT password FROM usuarios WHERE usuario = ?", (usuario,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return False
    return password == row[0]
