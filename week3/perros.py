class Perro:
    def __init__(self, nombre, altura, peso, raza):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso
        self.raza = raza

    def ladrar(self):
        if self.raza == "Labrador":
            print("Woof woof!")
        elif self.raza == "Beagle": 
            print("Guau guau!")
        
    def saludar(self):
        print("Hola, soy", self.nombre)
        
    def obtener_peso(self):
        return self.peso
      
mi_perro = Perro("Fido", 50, 20, "Labrador")
print(mi_perro.nombre) 
mi_perro.ladrar()
tu_perro = Perro("Ronaldito", "125 cm", "15.5 kg", "Beagle")
print(tu_perro.nombre) 
tu_perro.ladrar()
mi_perro.saludar()
print("Peso de mi perro:", tu_perro.obtener_peso())