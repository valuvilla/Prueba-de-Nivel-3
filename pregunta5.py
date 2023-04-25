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
        if(raiz is None):
            raiz = nodoArbol(dato)
        else:
            if(raiz.info > dato):
                raiz.izq = nodoArbol.insertar_nodo(raiz.izq, dato)
            else:
                raiz.der = nodoArbol.insertar_nodo(raiz.der, dato)
        raiz = nodoArbol.balancear(raiz)
        nodoArbol.actualizaraltura(raiz)
        return raiz
            
    def balancear(raiz):
        """Determina que rotación hay que hacer para balancear el árbol."""
        if(raiz is not None):
            if(nodoArbol.altura(raiz.izq)-nodoArbol.altura(raiz.der) == 2):
                if(nodoArbol.altura(raiz.izq.izq) >= nodoArbol.altura(raiz.izq.der)):
                    raiz = nodoArbol.rotar_simple(raiz, True)
                else:
                    raiz = nodoArbol.rotar_doble(raiz, True)
            elif(nodoArbol.altura(raiz.der)-nodoArbol.altura(raiz.izq) == 2):
                if(nodoArbol.altura(raiz.der.der) >= nodoArbol.altura(raiz.der.izq)):
                    raiz = nodoArbol.rotar_simple(raiz, False)
                else:
                    raiz = nodoArbol.rotar_doble(raiz, False)
        return raiz
    
    def rotar_simple(raiz, control):
        """Realiza una rotación simple de nodos a la derecha o a la izquierda."""
        if control:
            aux = raiz.izq
            raiz.izq = aux.der
            aux.der = raiz
        else:
            aux = raiz.der
            raiz.der = aux.izq
            aux.izq = raiz
        nodoArbol.actualizaraltura(raiz)
        nodoArbol.actualizaraltura(aux)
        raiz = aux
        return raiz

    def rotar_doble(raiz, control):
        """Realiza una rotación doble de nodos a la derecha o a la izquierda."""
        if control:
            raiz.izq = nodoArbol.rotar_simple(raiz.izq, False)
            raiz = nodoArbol.rotar_simple(raiz, True)
        else:
            raiz.der = nodoArbol.rotar_simple(raiz.der, True)
            raiz = nodoArbol.rotar_simple(raiz, False)
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
        raiz = nodoArbol.balancear(raiz)
        nodoArbol.actualizaraltura(raiz)
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
        cola = Cola()
        Cola.arribo(cola, raiz)
        while(not Cola.cola_vacia(cola)):
            nodo = Cola.atencion(cola)
            print(nodo.info)
            if(nodo.izq is not None):
                Cola.arribo(cola, nodo.izq)
            if(nodo.der is not None):
                Cola.arribo(cola, nodo.der)

    def busqueda(raiz, buscado):
        if(raiz is not None):
            if(raiz.info == buscado):
                return raiz
            else:
                if(raiz.info > buscado):         
                    return nodoArbol.busqueda(raiz.izq, buscado)
                else:
                    return nodoArbol.busqueda(raiz.der, buscado)
    
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
        """"Devuelve la altura del nodo"""
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





    
