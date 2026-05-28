from db.database import get_connection


def crear_induccion(candidato_id, tipo_induccion, responsable, temas_cubiertos):
    """Crear registro de inducción"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO induccion(candidato_id, tipo_induccion, fecha_induccion, responsable, temas_cubiertos, estado)
        VALUES(?, ?, datetime('now'), ?, ?, 'Completada')
        """,
        (candidato_id, tipo_induccion, responsable, temas_cubiertos)
    )
    conn.commit()
    conn.close()


def obtener_inducciones_por_candidato(candidato_id):
    """Obtener inducciones de un candidato"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM induccion WHERE candidato_id = ?", (candidato_id,))
    inducciones = cur.fetchall()
    conn.close()
    return inducciones


def obtener_todas_inducciones():
    """Obtener todas las inducciones"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT i.*, c.nombre FROM induccion i 
        JOIN candidatos c ON i.candidato_id = c.id
    """)
    inducciones = cur.fetchall()
    conn.close()
    return inducciones


def actualizar_induccion(induccion_id, temas_cubiertos, responsable):
    """Actualizar información de inducción"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE induccion SET temas_cubiertos = ?, responsable = ? WHERE id = ?",
        (temas_cubiertos, responsable, induccion_id)
    )
    conn.commit()
    conn.close()


def eliminar_induccion(induccion_id):
    """Eliminar un registro de inducción"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM induccion WHERE id = ?", (induccion_id,))
    conn.commit()
    conn.close()
