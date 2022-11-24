from ejercicio_clase import Vehiculo

class Coche(Vehiculo):

    def __init__(self,color,ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f" El coche avanza a una velocidad de {self.velocidad} km/h y tiene una cilindrada de {self.cilindrada}."

    def arrancar(self):
        return super().arrancar()

    def frenar(self):
        return super().frenar()