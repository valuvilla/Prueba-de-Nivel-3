import random
import sys
import unittest
from tda_colas import Cola

class nodoArbol(object):
    """clase nodo arbol"""

    def __init__(self, info):
        """crea un nodo con la informacion cargada"""
        self.info = info
        self.izq = None
        self.der = None
        self.altura = 0

    def insertar_nodo(raiz, dato):
        """Inserta un elemento en el árbol"""
        if (raiz is None):
            raiz = nodoArbol(dato)
        elif (dato < raiz.info):
            raiz.izq = nodoArbol.insertar_nodo(raiz.izq, dato)
        elif (dato > raiz.info):
            raiz.der = nodoArbol.insertar_nodo(raiz.der, dato)
        return raiz
            
        

    def eliminar_nodo(raiz, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra"""
       
        x=None
        if (raiz is not None):
            if (clave < raiz.info):
                raiz.izq, x =nodoArbol.eliminar_nodo(raiz.izq, clave)
            elif (clave > raiz.info):
                raiz.der, x = nodoArbol.eliminar_nodo(raiz.der, clave)
            else:
                x = raiz.info
                if (raiz.izq is None):
                    raiz = raiz.der
                elif (raiz.der is None):
                    raiz = raiz.izq
                else:
                    raiz.izq, aux = nodoArbol.reemplazar(raiz.izq)
                    raiz.info = aux.info
        return raiz, x


    def arbolvacio(raiz):
        """Verifica si el árbol está vacío"""
        return raiz is None

    def reemplazar(raiz):
        """"Determina el nodo que reemplaza al eliminado"""
        aux = None
        if raiz.der is None:
            aux = raiz
            raiz = raiz.izq
        else:
            raiz.der, aux = nodoArbol.reemplazar(raiz.der)
        return raiz, aux
    
    def por_nivel(raiz):
        """Realiza el barrido postorden del arbol"""
        pendientes = Cola()
        Cola.arribo(pendientes, raiz)
        while not Cola.cola_vacia(pendientes):
            nodo = Cola.atencion(pendientes)
            print(nodo.info)
            if nodo.izq is not None:
                Cola.arribo(pendientes, nodo.izq)
            if nodo.der is not None:
                Cola.arribo(pendientes, nodo.der)

    def buscar(raiz, clave):
        """Devuelve la direccion del elemeto buscado"""
        pos=None
        if (raiz is not None):
            if (raiz.info == clave):
                pos = raiz
            elif (clave < raiz.info):
                pos = nodoArbol.buscar(raiz.izq, clave)
            else:
                pos = nodoArbol.buscar(raiz.der, clave) 
        return pos
    
    def inorden(raiz):
        """Realiza el barrido inorden del arbol"""
        if (raiz is not None):
            nodoArbol.inorden(raiz.izq)
            print(raiz.info)
            nodoArbol.inorden(raiz.der)

    def imprimir_arbol_inorden_iterativo(raiz):
        pila = []
        nodo_actual = raiz
        while True:
            while nodo_actual:
                pila.append(nodo_actual)
                nodo_actual = nodo_actual.izq
            if not pila:
                return
            nodo_actual = pila.pop()
            print(nodo_actual.info)
            nodo_actual = nodo_actual.der

    

    def preorden(raiz):
        """Realiza el barrido preorden del arbol"""
        if (raiz is not None):
            print(raiz.info)
            nodoArbol.preorden(raiz.izq)
            nodoArbol.preorden(raiz.der)

    def postorden(raiz):
        """Realiza el barrido postorden del arbol"""
        if (raiz is not None):
            nodoArbol.postorden(raiz.izq)
            nodoArbol.postorden(raiz.der)
            print(raiz.info)

    def altura(raiz):
        """"DEvuelve la altura del nodo"""
        if (raiz is None):
            return -1
        else:
            return raiz.altura
    
    def actualizaraltura(raiz):
        """Actualiza la altura del nodo"""
        if (raiz is not None):
            alt_izq = nodoArbol.altura(raiz.izq)
            alt_der = nodoArbol.altura(raiz.der)
            raiz.altura= (alt_izq if alt_izq > alt_der else alt_der) + 1

    def impimir_arbol(raiz):
        """Imprime el arbol"""
        if (raiz is not None):
            nodoArbol.impimir_arbol(raiz.izq)
            print(raiz.info)
            nodoArbol.impimir_arbol(raiz.der)




raiz = None
# insertar los 1000 primeros números enteros
sys.setrecursionlimit(2000)

# GENERAR 1000 NUMEROS DE FORMA ALEATORIa
numeros_aleatorios = [random.randint(1, 1500) for _ in range(0,1001)]
for i in numeros_aleatorios:
    raiz=nodoArbol.insertar_nodo(raiz,i)

print(("INORDEN").center(50,'-'))
nodoArbol.inorden(raiz)

print("PREORDEN".center(50, '-'))
nodoArbol.inorden(raiz)

print("POSTORDEN".center(50,'-'))
nodoArbol.postorden(raiz)

print("POR NIVELES".center(50,'-'))
nodoArbol.por_nivel(raiz)

# Determinar si el albol esta cargado o no


    
