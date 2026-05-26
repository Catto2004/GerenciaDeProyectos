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

    # default admin
    cur.execute("SELECT COUNT(*) FROM usuarios WHERE usuario = ?", ("admin",))
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO usuarios(usuario,password) VALUES(?,?)", ("admin", "1234"))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print(f"Database initialized at: {DB_PATH}")
