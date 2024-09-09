# Classes

# Ejemplo con movimiento rectilineo uniforme (MRU) y movimiento rectilineo uniformemente acelerado (MRUA).

import matplotlib.pyplot as plt
import scienceplots
plt.style.use(["science", "notebook", "grid"])


class Particula:
    # Definir el constructor de la clase para una partícula para su estudio cinemático.
    def __init__(self, xi, vi, a):
        print("Se está creando un objeto partícula")
        self.xi = xi
        self.vi = vi
        self.a = a
        # Agregar la posición final (xf) y la velocidad final (vf) como un dato que se desconoce
        self.xf = None
        self.vf = None

    # Crear métodos que retornen los parámetros iniciales de la partícula.
    def get_xi(self):
        return self.xi

    def get_xf(self):
        return self.xf

    def get_vi(self):
        return self.vi

    def get_a(self):
        return self.a

    # Set a new initial position, velocity and acceleracion
    def set_xi(self, xi):
        self.xi = xi

    def set_vi(self, vi):
        self.vi = vi

    def set_a(self, a):
        self.a = a

    def move(self, time):
        self.xf = self.xi + self.vi*time + self.a * (time ** 2 / 2)
        return self.xf

    def get_vf(self, time):
        self.vf = self.vi + self.a * time
        return self.vf


# Inheritance (herencia)
# class Persona():
#     def __init__(self, nombre, documento, edad):
#         self.nombre = nombre
#         self.documento = documento
#         self.edad = edad
#
#     def ocupacion(self, profesion):
#         print(f"{self.nombre} es {self.profesion}")
#
#
# # Inherit from the class "Persona" to create a new class "Estudiante"
# class Estudiante(Persona):
#     def __init__(self, universidad):
#         self.universidad = universidad
#
#
# persona1 = Persona("carlos", 123, 23)
# estudiante1 = Estudiante("Oscar", 321, 20)


# Crear los objetos (partículas) de la clase
px = Particula(0, 0.7, 0)  # p1 es el auto que inicia desde el origen de coordenadas con una vi != 0
py = Particula(45, 0.7, -9.8)  # p2 es un camión que inicia desde el reposo pero a 2 metros desde el origen

# # Usar la notación de punto "." para acceder a los métodos de una clase.
# print(f"La posición inicial de la partícula es: {p1.get_xi()} m")
#
# # Agregar una nueva posición inicial
# p1.set_xi(8)
# print(f"La nueva posición inicial es de: {p1.get_xi()} m")
#
# # Calcular las posiciones finales de las partículas
# print(f"la posición final de la p1 transcurridos 4 s es de: {p1.move(4)} m")
# print(f"la posición final de la p2 transcurridos 4 s es de: {p2.move(4)} m")


# Definir en qué momento se encuentran p1 y p2
t = 0

while True:
    d = abs(px.move(t) - py.move(t))
    if d < 0.5:
        print(f"Los autos se encontraron en la coordenada x: {px.xf}, p1")
        print(f"Los autos se encontraron en la coordenada x: {py.xf}, p2")
        print(f"Se encuentran en t: {t} s")
        break

    t += 0.1
    if t > 1000:
        print(f"p1 y p2 no se encontraron en un lapso de tiempo de {t}")
        break

# Example of plotting
x = list()
y = list()

for t in range(10):
    x.append(px.move(t))
    y.append(py.move(t))

plt.plot(x, y)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()


# todo: crear un archivo de texto donde se almacenen los datos de t,x,y con cada simulación realizada.
