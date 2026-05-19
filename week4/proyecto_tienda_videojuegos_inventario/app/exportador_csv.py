import pandas as pd


class ExportadorCSV:
    def __init__(self, bd):
        self.bd = bd

    def exportar_ventas_por_ciudad(self):
        with self.bd.conectar() as conexion:
            query = """
            SELECT ciudad,
                   ROUND(SUM(total),2) AS total_ventas,
                   COUNT(*) AS cantidad_ventas
            FROM ventas
            GROUP BY ciudad
            ORDER BY total_ventas DESC
            """

            df = pd.read_sql_query(query, conexion)

            df.to_csv("reporte_ventas_ciudad.csv", index=False)

            print("\nCSV generado: reporte_ventas_ciudad.csv")
            print(df)

    def exportar_productos(self):
        with self.bd.conectar() as conexion:
            query = """
            SELECT producto,
                   SUM(cantidad) AS total_vendido,
                   ROUND(SUM(total),2) AS ingresos
            FROM ventas
            GROUP BY producto
            ORDER BY total_vendido DESC
            """

            df = pd.read_sql_query(query, conexion)

            df.to_csv("reporte_productos.csv", index=False)

            print("\nCSV generado: reporte_productos.csv")
            print(df.head())
