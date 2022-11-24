class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"El vehículo es de color {self.color} y tiene {self.ruedas} ruedas."

    def avanzar(self):
        pass


