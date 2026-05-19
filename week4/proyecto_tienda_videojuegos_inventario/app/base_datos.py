import sqlite3


class BaseDatos:
    def __init__(self, nombre_bd):
        self.nombre_bd = nombre_bd

    def conectar(self):
        return sqlite3.connect(self.nombre_bd)

    def crear_tablas(self):
        with self.conectar() as conexion:
            cursor = conexion.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ventas (
                id_venta INTEGER PRIMARY KEY,
                fecha_venta TEXT,
                nombre_cliente TEXT,
                ciudad TEXT,
                producto TEXT,
                categoria TEXT,
                cantidad INTEGER,
                precio_unitario REAL,
                metodo_pago TEXT,
                total REAL
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventario (
                producto TEXT PRIMARY KEY,
                categoria TEXT,
                stock INTEGER,
                precio_unitario REAL
            )
            """)
