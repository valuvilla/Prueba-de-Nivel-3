class NodoArbol(object):
    """clase para crear un nodo de un arbol"""

    def __init__(self, info):
        """crea un nodo con la informacion cargada"""
        self.info = info
        self.izq = None
        self.der = None

def insertar_marvel(raiz, pregunta, si, no):
    """inserta un nodo en el arbol"""
    if raiz is None:
        return NodoArbol(pregunta)
    else:
        if  respuesta == "si":
            raiz.izq = insertar_marvel(raiz.izq, si[0], si[1], si[2])
        else:
            raiz.der = insertar_marvel(raiz.der, no[0], no[1], no[2])
        return raiz

def buscar_marvel(raiz, pregunta):
    """busca un nodo en el arbol"""
    if raiz is None or raiz.info == pregunta:
        return raiz
    elif pregunta[0] == "si":
        return buscar_marvel(raiz.izq, pregunta[1])
    else:
        return buscar_marvel(raiz.der, pregunta[2])

arbol = NodoArbol("Preg1")
arbol.izq = NodoArbol("Preg2")
arbol.izq.izq = NodoArbol("Hulk")
arbol.izq.der = NodoArbol("Thor")
arbol.der = NodoArbol("Preg3")
arbol.der.izq = NodoArbol("IronMan")
arbol.der.der = NodoArbol("Capitan")

arbol = insertar_marvel(arbol, "¿El superhéroe tiene telarañas?", 
                        ["Spiderman", None, None], ["Capitan", None, None])
