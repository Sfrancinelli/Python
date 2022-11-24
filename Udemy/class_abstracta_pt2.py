from class_abstracta import Animal

class Gato(Animal):
    def mover(self):
        print('El gato se mueve.')

    def emitir_sonido(self):
        super().emitir_sonido()
        print('Miau!')