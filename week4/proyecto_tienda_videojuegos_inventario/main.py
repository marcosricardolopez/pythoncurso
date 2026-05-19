from config import ARCHIVO_CSV, ARCHIVO_INVENTARIO, NOMBRE_BD
from app.estadisticas import cargar_csv, mostrar_estadisticas
from app.base_datos import BaseDatos
from app.exportador_csv import ExportadorCSV
from app.inventario_servicio import InventarioServicio
import pandas as pd


def cargar_datos_sqlite(df, bd):
    with bd.conectar() as conexion:
        df.to_sql("ventas", conexion, if_exists="replace", index=False)

    print("\nDatos cargados correctamente en SQLite")


def main():
    # CSV
    df = cargar_csv(ARCHIVO_CSV)

    # Estadísticas
    mostrar_estadisticas(df)

    # SQLite
    bd = BaseDatos(NOMBRE_BD)
    bd.crear_tablas()

    cargar_datos_sqlite(df, bd)

    # Reportes
    exportador = ExportadorCSV(bd)

    exportador.exportar_ventas_por_ciudad()
    exportador.exportar_productos()

    # Inventario
    inventario = InventarioServicio(bd)

    inventario.crear_tabla_inventario()

    inventario.cargar_inventario(
        ARCHIVO_INVENTARIO
    )

    inventario.mostrar_inventario()

    inventario.validar_stock(
        "PlayStation 5",
        2
    )

    inventario.descontar_stock(
        "PlayStation 5",
        2
    )

    inventario.exportar_bajo_inventario()

    print("\nProyecto terminado correctamente")


if __name__ == "__main__":
    main()
