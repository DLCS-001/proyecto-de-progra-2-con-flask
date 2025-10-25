import sqlite3

def crear_tabla():
    conn = sqlite3.connect("Formulario.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS valoraciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            estrellas INTEGER NOT NULL CHECK(estrellas BETWEEN 0 AND 5),
            experiencia TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def guardar_valoracion(nombre, estrellas, experiencia):
    conn = sqlite3.connect("Formulario.db")
    c = conn.cursor()
    c.execute("INSERT INTO valoraciones (nombre, estrellas, experiencia) VALUES (?, ?, ?)",
              (nombre, estrellas, experiencia))
    conn.commit()
    conn.close()
