
from config import ARCHIVO_CSV, NOMBRE_BD
from app.estadisticas import cargar_csv, mostrar_estadisticas
from app.base_datos import BaseDatos
from app.exportador_csv import ExportadorCSV
import pandas as pd


def cargar_datos_sqlite(df, bd):
    with bd.conectar() as conexion:
        df.to_sql("ventas", conexion, if_exists="replace", index=False)

    print("\nDatos cargados correctamente en SQLite")


def main():
    df = cargar_csv(ARCHIVO_CSV)

    mostrar_estadisticas(df)

    bd = BaseDatos(NOMBRE_BD)
    bd.crear_tablas()

    cargar_datos_sqlite(df, bd)

    exportador = ExportadorCSV(bd)

    exportador.exportar_ventas_por_ciudad()
    exportador.exportar_productos()

    print("\nProyecto terminado correctamente")


if __name__ == "__main__":
    main()
