# Classes

# Ejemplo con movimiento rectilineo uniforme (MRU) y movimiento rectilineo uniformemente acelerado (MRUA).

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


# Crear los objetos (partículas) de la clase
p1 = Particula(0, 2, 9.8)  # p1 es el auto que inicia desde el origen de coordenadas con una vi != 0
p2 = Particula(2, 3, 0)  # p2 es un camión que inicia desde el reposo pero a 2 metros desde el origen

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
    d = abs(p1.move(t) - p2.move(t))
    if d < 0.5:
        print(f"Los autos se encontraron en la coordenada x: {p1.xf}, p1")
        print(f"Los autos se encontraron en la coordenada x: {p2.xf}, p2")
        print(f"Se encuentran en t: {t} s")
        break

    t += 0.1
    if t > 1000:
        print(f"p1 y p2 no se encontraron en un lapso de tiempo de {t}")
        break
