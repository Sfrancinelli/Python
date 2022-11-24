class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"El vehículo es {self.color} y tiene {self.ruedas} ruedas."
    
    def arrancar(self):
        print(f"El vehículo está arrancando.")
    
    def frenar(self):
        print(f"El vehículo ha frenado.")