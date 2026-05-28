"""Servicio de Pruebas Psicotécnicas."""
from db.database import get_connection


def crear_prueba_psicotecnica(candidato_id, tipo_prueba, resultado, puntaje, observaciones, evaluador):
    """Crear registro de prueba psicotécnica."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO pruebas_psicotecnicas(candidato_id, tipo_prueba, fecha_aplicacion, resultado, puntaje, observaciones, evaluador, estado)
        VALUES(?, ?, datetime('now'), ?, ?, ?, ?, 'Aplicada')
        """,
        (candidato_id, tipo_prueba, resultado, puntaje, observaciones, evaluador)
    )
    conn.commit()
    prueba_id = cur.lastrowid
    conn.close()
    return prueba_id


def obtener_todas_pruebas():
    """Obtener todas las pruebas psicotécnicas."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT pp.*, c.nombre FROM pruebas_psicotecnicas pp
        JOIN candidatos c ON pp.candidato_id = c.id
        ORDER BY pp.fecha_aplicacion DESC
    """)
    pruebas = cur.fetchall()
    conn.close()
    return pruebas


def obtener_pruebas_por_candidato(candidato_id):
    """Obtener pruebas de un candidato."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM pruebas_psicotecnicas WHERE candidato_id = ?", (candidato_id,))
    pruebas = cur.fetchall()
    conn.close()
    return pruebas


def eliminar_prueba(prueba_id):
    """Eliminar una prueba."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM pruebas_psicotecnicas WHERE id = ?", (prueba_id,))
    conn.commit()
    conn.close()
