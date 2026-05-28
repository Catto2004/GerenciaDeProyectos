from db.database import get_connection


def crear_afiliacion(candidato_id, tipo_afiliacion, entidad, numero_afiliacion):
    """Crear una afiliación (ARL, EPS, Caja Compensación)"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO afiliaciones(candidato_id, tipo_afiliacion, entidad, numero_afiliacion, fecha_afiliacion, estado)
        VALUES(?, ?, ?, ?, datetime('now'), 'Activa')
        """,
        (candidato_id, tipo_afiliacion, entidad, numero_afiliacion)
    )
    conn.commit()
    conn.close()


def obtener_afiliaciones_por_candidato(candidato_id):
    """Obtener todas las afiliaciones de un candidato"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM afiliaciones WHERE candidato_id = ?", (candidato_id,))
    afiliaciones = cur.fetchall()
    conn.close()
    return afiliaciones


def obtener_todas_afiliaciones():
    """Obtener todas las afiliaciones"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT a.*, c.nombre FROM afiliaciones a 
        JOIN candidatos c ON a.candidato_id = c.id
    """)
    afiliaciones = cur.fetchall()
    conn.close()
    return afiliaciones


def actualizar_estado_afiliacion(afiliacion_id, estado):
    """Actualizar estado de una afiliación"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE afiliaciones SET estado = ? WHERE id = ?", (estado, afiliacion_id))
    conn.commit()
    conn.close()


def eliminar_afiliacion(afiliacion_id):
    """Eliminar una afiliación"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM afiliaciones WHERE id = ?", (afiliacion_id,))
    conn.commit()
    conn.close()


def actualizar_afiliacion(afiliacion_id, entidad=None, numero_afiliacion=None):
    """Actualizar entidad y/o numero de una afiliación"""
    conn = get_connection()
    cur = conn.cursor()
    
    fields = []
    values = []
    
    if entidad is not None:
        fields.append("entidad = ?")
        values.append(entidad)
    if numero_afiliacion is not None:
        fields.append("numero_afiliacion = ?")
        values.append(numero_afiliacion)
    
    if not fields:
        # No changes requested - consider success
        conn.close()
        return True
    
    values.append(afiliacion_id)
    query = f"UPDATE afiliaciones SET {', '.join(fields)} WHERE id = ?"
    cur.execute(query, values)
    updated = cur.rowcount
    conn.commit()
    conn.close()
    return updated > 0
