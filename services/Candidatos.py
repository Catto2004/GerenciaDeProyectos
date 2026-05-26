from db.database import get_connection
from typing import List, Dict


def add_candidato(nombre: str, correo: str, telefono: str, estado: str = "Registrado") -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO candidatos(nombre, correo, telefono, estado) VALUES(?,?,?,?)",
        (nombre, correo, telefono, estado),
    )
    conn.commit()
    cid = cur.lastrowid
    conn.close()
    return cid


def list_candidatos() -> List[Dict]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, correo, telefono, estado FROM candidatos ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return [
        {"id": r[0], "nombre": r[1], "correo": r[2], "telefono": r[3], "estado": r[4]} for r in rows
    ]


def count_total() -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM candidatos")
    n = cur.fetchone()[0]
    conn.close()
    return n


def count_by_estado() -> Dict[str, int]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT estado, COUNT(*) FROM candidatos GROUP BY estado")
    rows = cur.fetchall()
    conn.close()
    return {r[0]: r[1] for r in rows}
