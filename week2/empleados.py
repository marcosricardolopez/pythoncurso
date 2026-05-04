empleados = [
    {
        "id": 1001,
        "nombre": "Ana",
        "departamento": "IT",
        "sueldo": 45000,
        "activo": True
    },
    {
        "id": 1002,
        "nombre": "Luis",
        "departamento": "HR",
        "sueldo": 32000,
        "activo": True
    },
    {
        "id": 1003,
        "nombre": "Pedro",
        "departamento": "Finance",
        "sueldo": 28000,
        "activo": False
    }
]


# Función para calcular bono
def calcular_bono(sueldo):
    if sueldo >= 40000:
        return sueldo * 0.10
    else:
        return sueldo * 0.05


# Función para mostrar empleado
def mostrar_empleado(emp):

    print("ID:", emp["id"])
    print("Nombre:", emp["nombre"])
    print("Departamento:", emp["departamento"])
    print("Sueldo:", emp["sueldo"])
    print("Activo:", emp["activo"])

    if emp["activo"]:
        bono = calcular_bono(emp["sueldo"])
        print("Bono:", bono)

    print("-------------------")


# Loop principal
for empleado in empleados:
    mostrar_empleado(empleado)