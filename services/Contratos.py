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


def list_contratados() -> List[Dict]:
    """Return list of contracted candidates with contract type and date."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT candidatos.id, candidatos.nombre, contratos.tipo, contratos.fecha
        FROM contratos
        JOIN candidatos ON contratos.candidato_id = candidatos.id
        ORDER BY contratos.id
        """
    )
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "nombre": r[1], "tipo": r[2], "fecha": r[3]} for r in rows]


def despedir_empleado(candidato_id: int) -> bool:
    """Fire an employee: delete their contracts and set candidate estado to 'Despedido'. Returns True if candidate existed."""
    conn = get_connection()
    cur = conn.cursor()
    # Delete contracts
    cur.execute("DELETE FROM contratos WHERE candidato_id = ?", (candidato_id,))
    # Update estado
    cur.execute("UPDATE candidatos SET estado = ? WHERE id = ?", ("Despedido", candidato_id))
    changed = cur.rowcount
    conn.commit()
    conn.close()
    return changed > 0


def seed_4_contratos() -> int:
    """Create four sample contracts for the first available candidates."""
    from datetime import date

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM candidatos ORDER BY id LIMIT 4")
    rows = cur.fetchall()
    if not rows:
        conn.close()
        return 0

    tipos = ["Temporal", "Indefinido", "Temporal", "Indefinido"]
    created = 0
    today = date.today().isoformat()
    for idx, row in enumerate(rows):
        candidato_id = row[0]
        tipo = tipos[idx % len(tipos)]
        cur.execute(
            "INSERT INTO contratos(candidato_id, fecha, tipo) VALUES(?,?,?)",
            (candidato_id, today, tipo),
        )
        cur.execute("UPDATE candidatos SET estado = ? WHERE id = ?", ("Contratado", candidato_id))
        created += 1
    conn.commit()
    conn.close()
    return created


def update_contrato(contrato_id: int, fecha: str = None, tipo: str = None) -> bool:
    """Update a contrato's information. Returns True if updated, False if not found."""
    conn = get_connection()
    cur = conn.cursor()
    
    # Build dynamic update query
    fields = []
    values = []
    
    if fecha is not None:
        fields.append("fecha = ?")
        values.append(fecha)
    if tipo is not None:
        fields.append("tipo = ?")
        values.append(tipo)
    
    if not fields:
        conn.close()
        return False
    
    values.append(contrato_id)
    query = f"UPDATE contratos SET {', '.join(fields)} WHERE id = ?"
    cur.execute(query, values)
    updated = cur.rowcount
    conn.commit()
    conn.close()
    return updated > 0


def get_contrato_by_id(contrato_id: int) -> Dict:
    """Get a contrato by ID."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, candidato_id, fecha, tipo FROM contratos WHERE id = ?", (contrato_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "candidato_id": row[1], "fecha": row[2], "tipo": row[3]}
    return None
