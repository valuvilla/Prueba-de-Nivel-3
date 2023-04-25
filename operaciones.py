# Crear con nodos y arboles un codigo que haga los cuatro operaciones básicas

class nodoArbol(object):
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None
        
def altura(raiz):
    """Devuelve la altura de un nodo."""
    if(raiz is None):
        return -1
    else:
        return raiz.altura


def actualizaraltura(raiz):
    """Actualiza la altura de un nodo."""
    if(raiz is not None):
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1

def insertar_nodo(raiz, dato):
    if(raiz is None):
        raiz = nodoArbol(dato)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = insertar_nodo(raiz.der, dato)
    raiz = balancear(raiz)
    actualizaraltura(raiz)
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
    actualizaraltura(raiz)
    actualizaraltura(aux)
    raiz = aux
    return raiz

def rotar_doble(raiz, control):
    """Realiza una rotación doble de nodos a la derecha o a la izquierda."""
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz


def balancear(raiz):
    """Determina que rotación hay que hacer para balancear el árbol."""
    if(raiz is not None):
        if(altura(raiz.izq)-altura(raiz.der) == 2):
            if(altura(raiz.izq.izq) >= altura(raiz.izq.der)):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif(altura(raiz.der)-altura(raiz.izq) == 2):
            if(altura(raiz.der.der) >= altura(raiz.der.izq)):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
    return raiz


def sumar(raiz):
    if(raiz is None):
        return 0
    else:
        #raiz=Excepciones(raiz)
        return raiz.info + sumar(raiz.izq) + sumar(raiz.der)

def restar(raiz):
    if(raiz is None):
        return 0
    else:
        raiz=Excepciones(raiz)
        return raiz.info - restar(raiz.izq) - restar(raiz.der)

def multiplicar(raiz):
    if(raiz is None):
        return 1
    else:
        raiz=Excepciones(raiz)
        return raiz.info * multiplicar(raiz.izq) * multiplicar(raiz.der)

def dividir(raiz):
    if(raiz is None):
        return 1
    else:
        raiz=Excepciones_división(raiz)
        return raiz.info / dividir(raiz.izq) / dividir(raiz.der)   

def Excepciones(raiz):
    # raise TypeError("El dato debe ser un número entero.")
    try:
        raiz.info = int(raiz.info)
        return raiz
    except ValueError:
        raise TypeError("El dato debe ser un número entero.")
    
def Excepciones_división(raiz):
    try:
        raiz.info = int(raiz.info)
        return raiz
    except ValueError:
        raise TypeError("El dato debe ser un número entero.")
    except ZeroDivisionError:
        raise TypeError("No se puede dividir entre cero.")
# ejemplos
raiz = None
raiz = insertar_nodo(raiz, 5)
raiz = insertar_nodo(raiz, 3)
sum=sumar(raiz)
rest=restar(raiz)
mul=multiplicar(raiz)
div=dividir(raiz)
print(sum)
print(rest)
print(mul)
print(div)

