"""Servicio de Verificación de Referencias."""
from db.database import get_connection


def crear_verificacion(candidato_id, nombre_referencia, telefono, empresa, cargo, relacionamento, verifica, observaciones):
    """Crear registro de verificación de referencias."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO verificacion_referencias(candidato_id, nombre_referencia, telefono, empresa, cargo, relacionamento, verifica, observaciones, fecha_verificacion, estado)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), 'Verificada')
        """,
        (candidato_id, nombre_referencia, telefono, empresa, cargo, relacionamento, verifica, observaciones)
    )
    conn.commit()
    verif_id = cur.lastrowid
    conn.close()
    return verif_id


def obtener_todas_verificaciones():
    """Obtener todas las verificaciones."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT vr.*, c.nombre FROM verificacion_referencias vr
        JOIN candidatos c ON vr.candidato_id = c.id
        ORDER BY vr.fecha_verificacion DESC
    """)
    verificaciones = cur.fetchall()
    conn.close()
    return verificaciones


def obtener_verificaciones_por_candidato(candidato_id):
    """Obtener verificaciones de un candidato."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM verificacion_referencias WHERE candidato_id = ?", (candidato_id,))
    verificaciones = cur.fetchall()
    conn.close()
    return verificaciones


def eliminar_verificacion(verificacion_id):
    """Eliminar una verificación."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM verificacion_referencias WHERE id = ?", (verificacion_id,))
    conn.commit()
    conn.close()
