import pandas as pd


class InventarioServicio:
    def __init__(self, bd):
        self.bd = bd

    def crear_tabla_inventario(self):
        with self.bd.conectar() as conexion:
            cursor = conexion.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventario (
                producto TEXT PRIMARY KEY,
                categoria TEXT,
                stock INTEGER,
                precio_unitario REAL
            )
            """)

        print("\nTabla inventario creada correctamente")

    def cargar_inventario(self, archivo_csv):
        df = pd.read_csv(archivo_csv)

        with self.bd.conectar() as conexion:
            df.to_sql(
                "inventario",
                conexion,
                if_exists="replace",
                index=False
            )

        print("\nInventario cargado correctamente")

    def mostrar_inventario(self):
        with self.bd.conectar() as conexion:
            query = """
            SELECT *
            FROM inventario
            ORDER BY stock ASC
            """

            df = pd.read_sql_query(query, conexion)

            print("\nINVENTARIO ACTUAL")
            print(df.to_string(index=False))

    def validar_stock(self, producto, cantidad):
        with self.bd.conectar() as conexion:
            cursor = conexion.cursor()

            cursor.execute("""
            SELECT stock
            FROM inventario
            WHERE producto = ?
            """, (producto,))

            resultado = cursor.fetchone()

            if resultado is None:
                print(f"\nEl producto {producto} no existe")
                return False

            stock_actual = resultado[0]

            print(f"\nStock actual de {producto}: {stock_actual}")

            if stock_actual >= cantidad:
                print("Stock suficiente")
                return True
            else:
                print("Stock insuficiente")
                return False

    def descontar_stock(self, producto, cantidad):
        if not self.validar_stock(producto, cantidad):
            print("\nNo se puede completar la venta")
            return

        with self.bd.conectar() as conexion:
            cursor = conexion.cursor()

            cursor.execute("""
            UPDATE inventario
            SET stock = stock - ?
            WHERE producto = ?
            """, (cantidad, producto))

        print(f"\nStock actualizado para {producto}")

    def exportar_bajo_inventario(self):
        with self.bd.conectar() as conexion:
            query = """
            SELECT *
            FROM inventario
            WHERE stock <= 10
            ORDER BY stock ASC
            """

            df = pd.read_sql_query(query, conexion)

            df.to_csv(
                "reporte_bajo_inventario.csv",
                index=False
            )

            print("\nCSV generado: reporte_bajo_inventario.csv")
            print(df.to_string(index=False))
