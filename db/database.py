import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "innovatech.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    """Create database and tables if they don't exist."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # usuarios
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY,
            usuario TEXT UNIQUE,
            password TEXT
        )
        """
    )
    # candidatos
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS candidatos(
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            correo TEXT,
            telefono TEXT,
            estado TEXT
        )
        """
    )
    # contratos
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS contratos(
            id INTEGER PRIMARY KEY,
            candidato_id INTEGER,
            fecha TEXT,
            tipo TEXT
        )
        """
    )
    # nomina (liquidación de nómina)
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS nomina(
            id INTEGER PRIMARY KEY,
            candidato_id INTEGER,
            periodo TEXT,
            salario_base REAL,
            descuentos REAL,
            bonificaciones REAL,
            total_liquido REAL,
            fecha_liquidacion TEXT,
            estado TEXT
        )
        """
    )
    # afiliaciones
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS afiliaciones(
            id INTEGER PRIMARY KEY,
            candidato_id INTEGER,
            tipo_afiliacion TEXT,
            entidad TEXT,
            numero_afiliacion TEXT,
            fecha_afiliacion TEXT,
            estado TEXT
        )
        """
    )
    # evaluaciones de desempeño
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS evaluaciones(
            id INTEGER PRIMARY KEY,
            candidato_id INTEGER,
            fecha_evaluacion TEXT,
            puntaje REAL,
            comentarios TEXT,
            evaluador TEXT,
            estado TEXT
        )
        """
    )
    # capacitaciones
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS capacitaciones(
            id INTEGER PRIMARY KEY,
            nombre_capacitacion TEXT,
            descripcion TEXT,
            fecha_inicio TEXT,
            fecha_fin TEXT,
            instructor TEXT,
            estado TEXT
        )
        """
    )
    # asistencia a capacitaciones
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS asistencia_capacitacion(
            id INTEGER PRIMARY KEY,
            capacitacion_id INTEGER,
            candidato_id INTEGER,
            asistio TEXT,
            calificacion REAL
        )
        """
    )
    # retiro de personal
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS retiro_personal(
            id INTEGER PRIMARY KEY,
            candidato_id INTEGER,
            fecha_retiro TEXT,
            motivo TEXT,
            liquidacion REAL,
            estado TEXT
        )
        """
    )
# inducción
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS induccion(
            id INTEGER PRIMARY KEY,
            candidato_id INTEGER,
            tipo_induccion TEXT,
            fecha_induccion TEXT,
            responsable TEXT,
            temas_cubiertos TEXT,
            estado TEXT
        )
        """
    )

    # certificaciones laborales
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS certificaciones_laborales(
            id INTEGER PRIMARY KEY,
            candidato_id INTEGER,
            tipo_certificacion TEXT,
            fecha_solicitud TEXT,
            fecha_emision TEXT,
            contenido TEXT,
            estado TEXT
        )
        """
    )

    # pruebas psicotécnicas
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS pruebas_psicotecnicas(
            id INTEGER PRIMARY KEY,
            candidato_id INTEGER,
            tipo_prueba TEXT,
            fecha_aplicacion TEXT,
            resultado TEXT,
            puntaje REAL,
            observaciones TEXT,
            evaluador TEXT,
            estado TEXT
        )
        """
    )

    # verificación de referencias
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS verificacion_referencias(
            id INTEGER PRIMARY KEY,
            candidato_id INTEGER,
            nombre_referencia TEXT,
            telefono TEXT,
            empresa TEXT,
            cargo TEXT,
            relacionamento TEXT,
            verifica TEXT,
            observaciones TEXT,
            fecha_verificacion TEXT,
            estado TEXT
        )
        """
    )

    # exámenes de retiro
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS examenes_retiro(
            id INTEGER PRIMARY KEY,
            candidato_id INTEGER,
            tipo_examen TEXT,
            fecha_programada TEXT,
            fecha_realizacion TEXT,
            resultado TEXT,
            observaciones TEXT,
            estado TEXT
        )
        """
    )

    # plan de capacitación
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS plan_capacitacion(
            id INTEGER PRIMARY KEY,
            anio INTEGER,
            necesidad TEXT,
            capacitacion_id INTEGER,
            objetivo TEXT,
            meta_asistentes INTEGER,
            presupuesto REAL,
            estado TEXT
        )
        """
    )

    # evaluación de eficacia de capacitación
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS evaluacion_eficacia(
            id INTEGER PRIMARY KEY,
            capacitacion_id INTEGER,
            candidato_id INTEGER,
            metodo_evaluacion TEXT,
            resultado TEXT,
            puntaje REAL,
            fecha_evaluacion TEXT,
            observaciones TEXT,
            estado TEXT
        )
        """
    )

    # default admin
    cur.execute("SELECT COUNT(*) FROM usuarios WHERE usuario = ?", ("admin",))
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO usuarios(usuario,password) VALUES(?,?)", ("admin", "1234"))

    conn.commit()
    conn.close()


def clear_business_data():
    """Remove application data from candidatos and contratos, preserving users."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM contratos")
    cur.execute("DELETE FROM candidatos")
    try:
        cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('contratos', 'candidatos')")
    except sqlite3.OperationalError:
        pass
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print(f"Database initialized at: {DB_PATH}")
