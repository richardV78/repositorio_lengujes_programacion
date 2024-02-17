# sistematico_sistemas_operativo
# Ejercicio 1: Definición de una clase básica
# Define una clase llamada `Rectangulo` que tenga dos atributos: `base` y `altura`. La clase debe tener un método para calcular el área del rectángulo.

lass Rectangulo:
    def __init__(self, base, altura):
            self.base = base
            self.altura = altura
            self.area = base*altura
    def calcular(self):
          print(f"la base del rectangulo es : {self.base} la altura del rectangulo es {self.altura}")
          print (f"el area del rectangulo es {self.area}")

# creo los objeros para calcular el area de diferentes rectangulo
rectangulo1 = Rectangulo(10,8)
rectangulo1.calcular()