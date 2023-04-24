# desarrollar un arbol que se mueve a la derecha si la respuesta es no y a la izquierda si la respuesta es si

class NodoArbol(object):
    """clase para crear un nodo de un arbol"""

    def __init__(self, info):
        """crea un nodo con la informacion cargada"""
        self.info = info
        self.izq = None
        self.der = None

def insertar_preguntas(raiz, dato):
    """inserta un nodo en el arbol"""
    if raiz is None:
        nuevo_nodo=NodoArbol(dato)
        return nuevo_nodo
    else:
        nodo_actual = raiz
        # si la respuesta a la pregunta es si mover a la izquierda
        while nodo_actual is not None:
            ultimo_nodo = nodo_actual
            if dato[0] == "si":
                nodo_actual = nodo_actual.izq
            # si la respuesta a la pregunta es no mover a la derecha
            else:
                nodo_actual = nodo_actual.der

def insertar_marvel(raiz, dato):
    """inserta un nodo en el arbol"""
    if raiz is None:
        nuevo_nodo=NodoArbol(dato)
        return nuevo_nodo
    else:
        nodo_actual = raiz
        # si la respuesta a la pregunta es si mover a la izquierda
        while nodo_actual is not None:
            ultimo_nodo = nodo_actual
            if dato[0] == "si":
                nodo_actual = nodo_actual.izq
            # si la respuesta a la pregunta es no mover a la derecha
            else:
                nodo_actual = nodo_actual.der

def buscar_marvel(raiz, dato):
    """busca un nodo en el arbol"""
    nodo_actual = raiz
    while nodo_actual is not None:
        if dato == nodo_actual.info:
            return nodo_actual
        # si la respuesta es si busca en el lado izquierdo
        if dato[0] == "si":
            nodo_actual = nodo_actual.izq
        # si la respuesta es no busca en el lado derecho
        else:
            nodo_actual = nodo_actual.der
    return None


# Crear el árbol binario
raiz = NodoArbol("¿El superhéroe es adecuado para misiones de destrucción?")

