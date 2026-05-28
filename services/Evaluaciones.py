from db.database import get_connection


def crear_evaluacion(candidato_id, puntaje, comentarios, evaluador):
    """Crear una evaluación de desempeño"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO evaluaciones(candidato_id, fecha_evaluacion, puntaje, comentarios, evaluador, estado)
        VALUES(?, datetime('now'), ?, ?, ?, 'Completada')
        """,
        (candidato_id, puntaje, comentarios, evaluador)
    )
    conn.commit()
    conn.close()


def obtener_evaluaciones_por_candidato(candidato_id):
    """Obtener todas las evaluaciones de un candidato"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM evaluaciones WHERE candidato_id = ?", (candidato_id,))
    evaluaciones = cur.fetchall()
    conn.close()
    return evaluaciones


def obtener_todas_evaluaciones():
    """Obtener todas las evaluaciones"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT e.*, c.nombre FROM evaluaciones e 
        JOIN candidatos c ON e.candidato_id = c.id
    """)
    evaluaciones = cur.fetchall()
    conn.close()
    return evaluaciones


def eliminar_evaluacion(evaluacion_id):
    """Eliminar una evaluación"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM evaluaciones WHERE id = ?", (evaluacion_id,))
    conn.commit()
    conn.close()
