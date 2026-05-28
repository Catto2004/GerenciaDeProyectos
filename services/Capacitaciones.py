from db.database import get_connection


def crear_capacitacion(nombre_capacitacion, descripcion, fecha_inicio, fecha_fin, instructor):
    """Crear una capacitación"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO capacitaciones(nombre_capacitacion, descripcion, fecha_inicio, fecha_fin, instructor, estado)
        VALUES(?, ?, ?, ?, ?, 'Programada')
        """,
        (nombre_capacitacion, descripcion, fecha_inicio, fecha_fin, instructor)
    )
    conn.commit()
    conn.close()


def obtener_todas_capacitaciones():
    """Obtener todas las capacitaciones"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM capacitaciones")
    capacitaciones = cur.fetchall()
    conn.close()
    return capacitaciones


def registrar_asistencia(capacitacion_id, candidato_id, asistio, calificacion):
    """Registrar asistencia a una capacitación"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO asistencia_capacitacion(capacitacion_id, candidato_id, asistio, calificacion)
        VALUES(?, ?, ?, ?)
        """,
        (capacitacion_id, candidato_id, asistio, calificacion)
    )
    conn.commit()
    conn.close()


def obtener_asistencia_por_capacitacion(capacitacion_id):
    """Obtener asistencia a una capacitación específica"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT ac.*, c.nombre FROM asistencia_capacitacion ac 
        JOIN candidatos c ON ac.candidato_id = c.id
        WHERE ac.capacitacion_id = ?
    """, (capacitacion_id,))
    asistencia = cur.fetchall()
    conn.close()
    return asistencia


def obtener_capacitaciones_por_candidato(candidato_id):
    """Obtener capacitaciones en las que participó un candidato"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT cap.* FROM capacitaciones cap
        JOIN asistencia_capacitacion ac ON cap.id = ac.capacitacion_id
        WHERE ac.candidato_id = ?
    """, (candidato_id,))
    capacitaciones = cur.fetchall()
    conn.close()
    return capacitaciones


def actualizar_estado_capacitacion(capacitacion_id, estado):
    """Actualizar estado de una capacitación"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE capacitaciones SET estado = ? WHERE id = ?", (estado, capacitacion_id))
    conn.commit()
    conn.close()
