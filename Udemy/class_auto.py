from class_vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self,color,ruedas,cil):
        Vehiculo.__init__(self,color,ruedas)
        self.cilindrada = cil

    def __str__(self):
        return super().__str__() + ' Cilindrada: ' + str(self.cilindrada)

    def avanzar(self):
        super().avanzar()
        print("El auto avanza.")

def __main__():
    auto1 = Auto('Gris plata', 4, 1200)
    print(auto1)
    auto1.avanzar()

if __name__ == '__main__':
    __main__()

    print(__name__)