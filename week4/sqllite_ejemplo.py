import sqlite3

# Crear o abrir base de datos
conexion = sqlite3.connect("videojuegos.db")

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS videojuegos (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    precio REAL
)
""")

# Insertar datos
cursor.execute("""
INSERT INTO videojuegos (nombre, precio)
VALUES (?, ?)
""", ("PlayStation 5", 12000))

cursor.execute("""
INSERT INTO videojuegos (nombre, precio)
VALUES (?, ?)
""", ("Nintendo Switch", 7000))

cursor.execute("""
INSERT INTO videojuegos (nombre, precio)
VALUES (?, ?)
""", ("Xbox Series X", 15000))

# Guardar cambios
conexion.commit()

# Consultar datos
cursor.execute("SELECT *  FROM videojuegos")

datos = cursor.fetchall()

# Mostrar resultados
print("\nLISTA DE VIDEOJUEGOS")

for juego in datos:
    print(juego)

cursor.execute("""
DROP TABLE IF EXISTS videojuegos
""")

# Cerrar conexión
conexion.close()