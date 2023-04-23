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
    nuevo_nodo=NodoArbol(dato)
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
    if raiz is None:
        return None
    else:
        while raiz is not None:
            # si la respuesta a la pregunta es si mover a la izquierda
            if dato[0] == "si":
                buscar_marvel(raiz.izq, dato)
            # si la respuesta a la pregunta es no mover a la derecha
            else:
                buscar_marvel(raiz.der, dato)
            
    



# Agregar los superheroes
raiz =NodoArbol("¿Es una excelente opción para misiones de destrucción de ejercitos completos?")
insertar_marvel(raiz, ("si", "Thor"))

print(buscar_marvel(raiz, "¿Es una excelente opción para misiones de destrucción de ejercitos completos?"))