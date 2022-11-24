from ejercicio_clase import Vehiculo
from class_coche import Coche

class Camioneta(Coche, Vehiculo):
    
    def __init__(self,color,ruedas,velocidad,cilindrada, carga):
        Vehiculo.__init__(self,color,ruedas)
        Coche.__init__(self,color,ruedas,velocidad,cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f" Posee una capacidad de carga de {self.carga} kilogramos."

    def arrancar(self):
        return super().arrancar()

    def frenar(self):
        return super().frenar()

    def cargar(self):
        return f"La camioneta está cargando {self.carga} kilos."