import csv

# Función para calcular bono
def calcular_bono(sueldo):
    sueldo = float(sueldo)

    if sueldo >= 40000:
        return sueldo * 0.10
    else:
        return sueldo * 0.05


# Leer CSV
with open("C:/temp/pyexer/empleados.csv", newline="", encoding="utf-8") as archivo:

    lector = csv.DictReader(archivo)

    for empleado in lector:

        print("ID:", empleado["id"])
        print("Nombre:", empleado["nombre"])
        print("Departamento:", empleado["departamento"])
        print("Sueldo:", empleado["sueldo"])
        print("Activo:", empleado["activo"])

        if empleado["activo"] == "True":
            bono = calcular_bono(empleado["sueldo"])
            print("Bono:", bono)

        print("-------------------")