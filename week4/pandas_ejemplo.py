import pandas as pd

# Leer archivo JSON
df = pd.read_json("videojuegos.json")

# Mostrar primeras filas
print("\nPRIMERAS FILAS")
print(df.head())

# Mostrar estadísticas
print("\nTOTAL PRECIOS")
print(df["precio"].sum())

print("\nPROMEDIO PRECIOS")
print(df["precio"].mean())

print("\nPRODUCTO MÁS CARO")
print(df["precio"].max())

# Agrupar datos
print("\nCANTIDAD TOTAL POR PRODUCTO")
print(
    df.groupby("producto")["cantidad"]
    .sum()
    .to_string()
)