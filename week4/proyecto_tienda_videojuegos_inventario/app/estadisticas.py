import pandas as pd


def cargar_csv(archivo_csv):
    df = pd.read_csv(archivo_csv)

    print("\nPRIMERAS 5 FILAS")
    print(df.head())

    return df


def mostrar_estadisticas(df):
    print("\nESTADISTICAS")
    print("-" * 40)

    print(f"Total ventas: {len(df)}")
    print(f"Ventas totales: ${df['total'].sum():,.2f}")

    print("\nVENTAS POR CIUDAD")
    print(
        df.groupby("ciudad")["total"]
        .sum()
        .sort_values(ascending=False)
        .to_string()
    )

    print("\nTOP PRODUCTOS")
    print(
        df.groupby("producto")["cantidad"]
        .sum()
        .sort_values(ascending=False)
        .head()
        .to_string()
    )
