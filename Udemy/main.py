from class_auto import Auto
from class_abstracta import Animal
from class_abstracta_pt2 import Gato
from class_abstracta_pt3 import Perro

def __main__():
    auto1 = Auto('Rojo',4,1200)
    print(auto1)
    auto1.avanzar()

    a1 = Perro()
    a1.emitir_sonido()

    a2 = Gato()
    a2.emitir_sonido()

    animales = []
    animales.append(a1)
    animales.append(a2)

    print('')

    for animal in animales:
        animal.emitir_sonido()

if __name__ == '__main__':
    __main__()