from db.database import get_connection
from typing import List, Dict


def generar_contrato(candidato_id: int, fecha: str, tipo: str) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contratos(candidato_id, fecha, tipo) VALUES(?,?,?)",
        (candidato_id, fecha, tipo),
    )
    conn.commit()
    cid = cur.lastrowid
    conn.close()
    # update candidato estado a Contratado
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE candidatos SET estado = ? WHERE id = ?", ("Contratado", candidato_id))
    conn.commit()
    conn.close()
    return cid


def list_contratos() -> List[Dict]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, candidato_id, fecha, tipo FROM contratos ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "candidato_id": r[1], "fecha": r[2], "tipo": r[3]} for r in rows]


def count_total() -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM contratos")
    n = cur.fetchone()[0]
    conn.close()
    return n
