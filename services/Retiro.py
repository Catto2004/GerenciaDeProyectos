from db.database import get_connection


def crear_retiro(candidato_id, motivo, liquidacion):
    """Crear registro de retiro de personal"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO retiro_personal(candidato_id, fecha_retiro, motivo, liquidacion, estado)
        VALUES(?, datetime('now'), ?, ?, 'Pendiente')
        """,
        (candidato_id, motivo, liquidacion)
    )
    conn.commit()
    conn.close()


def obtener_retiros():
    """Obtener todos los retiros"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT r.*, c.nombre FROM retiro_personal r 
        JOIN candidatos c ON r.candidato_id = c.id
    """)
    retiros = cur.fetchall()
    conn.close()
    return retiros


def actualizar_estado_retiro(retiro_id, estado):
    """Actualizar estado de retiro"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE retiro_personal SET estado = ? WHERE id = ?", (estado, retiro_id))
    conn.commit()
    conn.close()


def obtener_retiros_por_candidato(candidato_id):
    """Obtener retiros de un candidato específico"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM retiro_personal WHERE candidato_id = ?", (candidato_id,))
    retiros = cur.fetchall()
    conn.close()
    return retiros


def eliminar_retiro(retiro_id):
    """Eliminar un retiro"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM retiro_personal WHERE id = ?", (retiro_id,))
    conn.commit()
    conn.close()
