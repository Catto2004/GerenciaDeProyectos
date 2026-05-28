from db.database import get_connection


def crear_liquidacion_nomina(candidato_id, periodo, salario_base, descuentos, bonificaciones):
    """Crear una liquidación de nómina"""
    conn = get_connection()
    cur = conn.cursor()
    total_liquido = salario_base - descuentos + bonificaciones
    cur.execute(
        """
        INSERT INTO nomina(candidato_id, periodo, salario_base, descuentos, bonificaciones, total_liquido, fecha_liquidacion, estado)
        VALUES(?, ?, ?, ?, ?, ?, datetime('now'), 'Liquidada')
        """,
        (candidato_id, periodo, salario_base, descuentos, bonificaciones, total_liquido)
    )
    conn.commit()
    conn.close()


def obtener_nominas_por_candidato(candidato_id):
    """Obtener todas las nóminas de un candidato"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM nomina WHERE candidato_id = ?", (candidato_id,))
    nominas = cur.fetchall()
    conn.close()
    return nominas


def obtener_todas_nominas():
    """Obtener todas las nóminas"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT n.*, c.nombre FROM nomina n 
        JOIN candidatos c ON n.candidato_id = c.id
    """)
    nominas = cur.fetchall()
    conn.close()
    return nominas


def eliminar_liquidacion_nomina(nomina_id):
    """Eliminar una liquidación de nómina"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM nomina WHERE id = ?", (nomina_id,))
    conn.commit()
    conn.close()
