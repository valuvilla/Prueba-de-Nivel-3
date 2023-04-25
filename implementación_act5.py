import random
import sys

from pregunta5 import nodoArbol


raiz = None
# insertar los 1000 primeros números enteros
sys.setrecursionlimit(5000)

# GENERAR 1000 NUMEROS DE FORMA ALEATORIa
numeros_aleatorios = [random.randint(1, 1500) for _ in range(10)] # porque razon se debe poner 1003 para conseguir 1000 numeros
for i in numeros_aleatorios:
    raiz=nodoArbol.insertar_nodo(raiz,i)

print(("INORDEN").center(50,'-'))
nodoArbol.inorden(raiz)

print("PREORDEN".center(50, '-'))
#nodoArbol.inorden(raiz)

print("POSTORDEN".center(50,'-'))
#nodoArbol.postorden(raiz)

print("POR NIVELES".center(50,'-'))
#nodoArbol.por_nivel(raiz)

# Determinar si un número esta cargado en el arbol o no
# buscar en el arbol
numero_a_buscar=int(input("Número a buscar: "))
respuesta=nodoArbol.busqueda(raiz,numero_a_buscar)
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
alt_izq=nodoArbol.altura(raiz.izq)
alt_der=nodoArbol.altura(raiz.der)
print(f'La altura del subarbol derecho es {alt_der} y la del izquierdo es {alt_izq}')


    
# Determinar las ocurrencias de un valor en el arbol
print("Ocurrencias de un valor en el arbol")
valor=int(input("Valor a buscar: "))
ocurrencias=nodoArbol.contar_ocurrencias(raiz, valor)
print(f'El valor {valor} se repite {ocurrencias} veces')


# Contar cuántos números pares e impares hay en el árbol
print("Contar cuántos números pares e impares hay en el árbol")
pares=nodoArbol.contar_pares(raiz)
impares=nodoArbol.contar_impares(raiz)
ceros=nodoArbol.contar_ceros(raiz)
print(pares+impares+ceros)
print(f'Hay {pares} números pares y {impares} números impares')