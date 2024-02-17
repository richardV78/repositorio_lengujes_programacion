class Persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad 
    def saludar(self):
        print(f"hola, soy {self.nombre} y tengo {self.edad} años.")

#crear objeto
persona1 = Persona ("richard",19)
persona1.saludar()

mama=Persona("juana",38)
mama.saludar()

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def estudiar(self):
        print(f"{self.nombre} esta estudiando el grado {self.grado}.")

Estudiante1 = Estudiante("gabriela",22, "maestria")
Estudiante1.saludar()
Estudiante1.estudiar()
