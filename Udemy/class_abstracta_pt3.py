from class_abstracta import Animal

class Perro(Animal):
    def mover(self):
        print('El perro se mueve.')

    def emitir_sonido(self):
        super().emitir_sonido()
        print('Guau!')