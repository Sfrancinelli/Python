from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def mover():
        pass

    @abstractmethod
    def emitir_sonido(self):
        print('Animal emite sonido: ', end='')

