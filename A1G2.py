# pryecto A1G2
#Importamos la función bienvenida
#Importamos la función ing2i
#Importamos la función ing2s

from Funciones.presentacion import presentacion
from Funciones.ing2i import ing2i
from Funciones.ing2s import ing2s

presentacion()

enteros = ing2i()
print('Los enteros ingresados son: ', enteros[0], enteros[1])

strings = ing2s()
print('Los strings ingresados son: ', strings[0], strings[1])