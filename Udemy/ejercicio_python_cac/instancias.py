from ejercicio_clase import Vehiculo
from class_coche import Coche
from class_camioneta import Camioneta

vehiculos = []

def catalogar(vehiculo, ruedas = 4):
    vehiculos.append(vehiculo)

def __name__():

    camio1 = Camioneta("Gris",6,95,1600,2000)
    # print(camio1.cargar())
    # print(camio1.arrancar())
    # print(camio1)

    catalogar(camio1)

    coche1 = Coche("Rojo",4,185,1200)
    # print(coche1)
    # print(coche1.arrancar())

    catalogar(coche1)

    for i in vehiculos:
        clase = type(i).__name__
        print(clase)
        for att in dir(i):
            print(att, getattr(i, att)) and not att.startswith("__")
        # method_list = [func for func in dir(clase) if callable(getattr(clase, func)) and not func.startswith("__")]
        # print(method_list)

    # method_list = [func for func in dir(Coche) if callable(getattr(Coche, func)) and not func.startswith("__")]

    # print(method_list)

__name__()

