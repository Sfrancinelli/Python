import random
# Importar un modulo para usarlo desde otro archivo
import my_module
 
random_integer = random.randint(1,10)

print(random_integer)

# utilizar algun tipo de dato, funcion etc, que se encuentre en un modulo. 
# Para utilizarlo debemos definirlo mediante la nomenclatura del punto.
print(my_module.pi)

random_float = random.random()*5

print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")