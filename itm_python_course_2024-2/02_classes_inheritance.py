# Inheritance (herencia)

class Persona():
    def __init__(self, nombre, documento, edad):
        self.nombre = nombre
        self.documento = documento
        self.edad = edad

    def ocupacion(self, profesion):
        print(f"{self.nombre} es {self.profesion}")


# Inherit from the class "Persona" to create a new class "Estudiante"
class Estudiante(Persona):
    def __init__(self, universidad):
        self.universidad = universidad


persona1 = Persona("carlos", 123, 23)
estudiante1 = Estudiante("Oscar", 321, 20)
