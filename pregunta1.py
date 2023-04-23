# desarrollar un arbol que se mueve a la derecha si la respuesta es no y a la izquierda si la respuesta es si

class NodoArbol(object):
    """clase para crear un nodo de un arbol"""

    def __init__(self, info):
        """crea un nodo con la informacion cargada"""
        self.info = info
        self.izq = None
        self.der = None
        self.altura = 0

def insertar_marvel(raiz, dato):
    """inserta un nodo en el arbol"""
    if raiz is None:
        return NodoArbol(dato)
    else:
        # si la respuesta a la pregunta es si mover a la izquierda
        if dato[0] == "si":
            raiz.izq = insertar_marvel(raiz.izq, dato)
        # si la respuesta a la pregunta es no mover a la derecha
        else:
            raiz.der = insertar_marvel(raiz.der, dato)
    return raiz

def buscar_marvel(raiz, dato):
    """busca un nodo en el arbol"""
    if raiz is None:
        return None
    else:
        if raiz.info[1] == dato:
            return raiz.info
        else:
            # si la respuesta a la pregunta es si mover a la izquierda
            if dato[0] == "si":
                return buscar_marvel(raiz.izq, dato)
            # si la respuesta a la pregunta es no mover a la derecha
            else:
                return buscar_marvel(raiz.der, dato)


# Agregar los superheroes
raiz = NodoArbol("¿Es un superheroe?")



