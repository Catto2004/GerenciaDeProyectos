"""Servicio de Exámenes de Retiro."""
from db.database import get_connection


def crear_examen_retiro(candidato_id, tipo_examen, fecha_programada):
    """Crear examen de retiro."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO examenes_retiro(candidato_id, tipo_examen, fecha_programada, estado)
        VALUES(?, ?, ?, 'Programado')
        """,
        (candidato_id, tipo_examen, fecha_programada)
    )
    conn.commit()
    exam_id = cur.lastrowid
    conn.close()
    return exam_id


def obtener_todos_examenes():
    """Obtener todos los exámenes de retiro."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT er.*, c.nombre FROM examenes_retiro er
        JOIN candidatos c ON er.candidato_id = c.id
        ORDER BY er.fecha_programada DESC
    """)
    examenes = cur.fetchall()
    conn.close()
    return examenes


def obtener_examenes_por_candidato(candidato_id):
    """Obtener exámenes de un candidato."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM examenes_retiro WHERE candidato_id = ?", (candidato_id,))
    examenes = cur.fetchall()
    conn.close()
    return examenes


def actualizar_resultado_examen(examen_id, resultado, observaciones):
    """Actualizar resultado del examen."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE examenes_retiro 
        SET resultado = ?, observaciones = ?, fecha_realizacion = datetime('now'), estado = 'Realizado'
        WHERE id = ?
    """, (resultado, observaciones, examen_id))
    conn.commit()
    conn.close()


def eliminar_examen(examen_id):
    """Eliminar un examen."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM examenes_retiro WHERE id = ?", (examen_id,))
    conn.commit()
    conn.close()
