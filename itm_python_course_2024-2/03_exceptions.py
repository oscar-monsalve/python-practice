# Exceptions in python

# Una excepción es un evento que ocurre durante la ejecución del programa. Habitualmente, las exepciones tienen que
# ver con situaciones anómalas.


# Crear una excepción personalizada utilizando una clase y herencia de la clase "Exception"
class ErrorPersonalizado(Exception):
    def __init__(self, mensaje, informacion):
        self.mensaje = mensaje
        self.informacion = informacion


def dividir(a: float, b: float) -> float:
    return a / b


# Puede ocurrir que el denominador de la división sea cero (0) o por un carácter ("a")
a = 3
b = 1

try:
    res = dividir(a, b)
    if res == 3:
        raise ErrorPersonalizado("La razón es 3.", "Corrija la entrada.")
except ErrorPersonalizado as err:
    print(err.mensaje, err.informacion)
except ZeroDivisionError:
    print("División por cero")
except TypeError:
    print("División por un carácter")
else:
    print("No hay nada raro")
    print(f"El resultado es: {res}")
finally:
    print("Fin del programa")
