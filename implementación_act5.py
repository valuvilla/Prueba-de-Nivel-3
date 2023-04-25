import random
import sys

from pregunta5 import nodoArbol


raiz = None
# insertar los 1000 primeros números enteros
sys.setrecursionlimit(2000)

# GENERAR 1000 NUMEROS DE FORMA ALEATORIa
numeros_aleatorios = [random.randint(1, 1500) for _ in range(0,1001)]
for i in numeros_aleatorios:
    raiz=nodoArbol.insertar_nodo(raiz,i)

print(("INORDEN").center(50,'-'))
#nodoArbol.inorden(raiz)

print("PREORDEN".center(50, '-'))
#nodoArbol.inorden(raiz)

print("POSTORDEN".center(50,'-'))
#nodoArbol.postorden(raiz)

print("POR NIVELES".center(50,'-'))
#nodoArbol.por_nivel(raiz)

# Determinar si un número esta cargado en el arbol o no
# buscar en el arbol
numero_a_buscar=int(input("Número a buscar: "))
respuesta=nodoArbol.buscar(raiz,numero_a_buscar)
if respuesta is not None:
    print(f'El numero {numero_a_buscar} está en la lista')
else:
    print(f'El numero {numero_a_buscar} no esta en la lista')



# Eliminar tres valores del arbol
for i in range(1,4):
    raiz, dato= nodoArbol.eliminar_nodo(raiz, random.choice(numeros_aleatorios))
    if dato is not None:
        print("El dato eliminado es: ", dato)

# Determinar la altura del subarbol izquiedo y el subarbol derecho
nodoArbol.altura()


    
