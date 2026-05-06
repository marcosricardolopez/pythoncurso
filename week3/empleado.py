empleados_data = [
    {"nombre": "Ana", "salario": 1000},
    {"nombre": "Luis", "salario": 1500},
    {"nombre": "Pedro", "salario": 800}
]

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def aumentar_salario(self):
        self.salario += 100

    def mostrar(self):
        print(self.nombre, "- Salario:", self.salario)
        
class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = [] 

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def aumentar_salarios(self):
        for emp in self.empleados:
            emp.aumentar_salario()

    def mostrar_empleados(self):
        print("\nDepartamento:", self.nombre)
        for emp in self.empleados:
            emp.mostrar()

empleados = []

for emp in empleados_data:
    empleado = Empleado(emp["nombre"], emp["salario"])
    empleados.append(empleado)

for emp in empleados:
    emp.aumentar_salario()

for emp in empleados:
    emp.mostrar()
 

dep = Departamento("IT")

for emp in empleados:
    dep.agregar_empleado(emp)
    
dep.aumentar_salarios()

dep.mostrar_empleados()