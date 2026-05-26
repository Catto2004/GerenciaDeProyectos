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


def seed_candidatos() -> int:
    """Insert a small set of sample candidates if they do not already exist."""
    ejemplos = [
        ("Juan Perez", "juan.perez@example.com", "3001112233", "Registrado"),
        ("Maria Gomez", "maria.gomez@example.com", "3002223344", "Evaluado"),
        ("Pedro Ruiz", "pedro.ruiz@example.com", "3003334455", "Contratado"),
    ]

    conn = get_connection()
    cur = conn.cursor()
    insertados = 0
    for nombre, correo, telefono, estado in ejemplos:
        cur.execute("SELECT 1 FROM candidatos WHERE correo = ?", (correo,))
        if cur.fetchone() is None:
            cur.execute(
                "INSERT INTO candidatos(nombre, correo, telefono, estado) VALUES(?,?,?,?)",
                (nombre, correo, telefono, estado),
            )
            insertados += 1
    conn.commit()
    conn.close()
    return insertados


def seed_10_candidatos() -> int:
    """Insert ten sample candidates, replacing the earlier small sample set."""
    ejemplos = [
        ("Juan Perez", "juan.perez@example.com", "3001112233", "Registrado"),
        ("Maria Gomez", "maria.gomez@example.com", "3002223344", "Evaluado"),
        ("Pedro Ruiz", "pedro.ruiz@example.com", "3003334455", "Contratado"),
        ("Laura Torres", "laura.torres@example.com", "3004445566", "Registrado"),
        ("Carlos Diaz", "carlos.diaz@example.com", "3005556677", "Registrado"),
        ("Ana Lopez", "ana.lopez@example.com", "3006667788", "Evaluado"),
        ("Sofia Rojas", "sofia.rojas@example.com", "3007778899", "Registrado"),
        ("Diego Martinez", "diego.martinez@example.com", "3008889900", "Registrado"),
        ("Valentina Castro", "valentina.castro@example.com", "3010001122", "Evaluado"),
        ("Andres Moreno", "andres.moreno@example.com", "3011112233", "Registrado"),
    ]

    conn = get_connection()
    cur = conn.cursor()
    insertados = 0
    for nombre, correo, telefono, estado in ejemplos:
        cur.execute(
            "INSERT INTO candidatos(nombre, correo, telefono, estado) VALUES(?,?,?,?)",
            (nombre, correo, telefono, estado),
        )
        insertados += 1
    conn.commit()
    conn.close()
    return insertados


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


def delete_candidato(candidato_id: int) -> bool:
    """Delete a candidato and any related contracts. Returns True if a row was deleted."""
    conn = get_connection()
    cur = conn.cursor()
    # Remove contratos first to keep DB consistent
    cur.execute("DELETE FROM contratos WHERE candidato_id = ?", (candidato_id,))
    cur.execute("DELETE FROM candidatos WHERE id = ?", (candidato_id,))
    deleted = cur.rowcount
    conn.commit()
    conn.close()
    return deleted > 0
