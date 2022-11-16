class Gato:
    cont_gatos = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Gato.cont_gatos += 1

    def cumplir_anios(self):
        self.edad += 1

    def miau(self):
        return f'{self.nombre} dice "miau miau".'
    
    def __str__(self):
        '''Función que se encarga de brindar infromación del objeto mediante texto. Similar al "tostring" en otros lenguajes.'''
        return f"{self.nombre} tiene {self.edad} :)"

# Programa ppal
gato1 = Gato('Vainilla', 2)
gato2 = Gato('Mushu', 1)
gato1.cumplir_anios()
print(gato1)
print(gato2)

gato1.edad = 15
print(gato1)
print(gato1.edad)

print(gato1.miau())
print(gato2.miau())

def cargar_mascotas():
    lista = []
    nom = input("Ingrese nombre: ")
    while nom != '':
        edad = int(input("Ingrese edad: "))
        gato = Gato(nom, edad)
        lista.append(gato)
        nom = input("Ingrese nombre: ")
    return lista
    
def mostrar_lista(lista):
    for elem in lista:
        print(elem)

mascotas = cargar_mascotas()
print(mascotas)
mostrar_lista(mascotas)

print(f"creaste: {Gato.cont_gatos} gatos!")

