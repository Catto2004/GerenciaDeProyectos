"""Servicio de Certificaciones Laborales."""
from db.database import get_connection


def crear_certificacion(candidato_id, tipo_certificacion, contenido):
    """Crear una certificación laboral."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO certificaciones_laborales(candidato_id, tipo_certificacion, fecha_solicitud, contenido, estado)
        VALUES(?, ?, datetime('now'), ?, 'Pendiente')
        """,
        (candidato_id, tipo_certificacion, contenido)
    )
    conn.commit()
    cert_id = cur.lastrowid
    conn.close()
    return cert_id


def obtener_todas_certificaciones():
    """Obtener todas las certificaciones."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT cl.*, c.nombre FROM certificaciones_laborales cl
        JOIN candidatos c ON cl.candidato_id = c.id
        ORDER BY cl.fecha_solicitud DESC
    """)
    certificaciones = cur.fetchall()
    conn.close()
    return certificaciones


def obtener_certificaciones_por_candidato(candidato_id):
    """Obtener certificaciones de un candidato."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM certificaciones_laborales WHERE candidato_id = ?", (candidato_id,))
    certificaciones = cur.fetchall()
    conn.close()
    return certificaciones


def actualizar_estado_certificacion(certificacion_id, estado):
    """Actualizar estado de certificación."""
    conn = get_connection()
    cur = conn.cursor()
    if estado == "Emitida":
        cur.execute("UPDATE certificaciones_laborales SET estado = ?, fecha_emision = datetime('now') WHERE id = ?", 
                   (estado, certificacion_id))
    else:
        cur.execute("UPDATE certificaciones_laborales SET estado = ? WHERE id = ?", (estado, certificacion_id))
    conn.commit()
    conn.close()


def eliminar_certificacion(certificacion_id):
    """Eliminar una certificación."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM certificaciones_laborales WHERE id = ?", (certificacion_id,))
    conn.commit()
    conn.close()
