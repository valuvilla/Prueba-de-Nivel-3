from operaciones import *

a,b,c,d = (10,5,0,"Hola")
# pasar todo a string
a, b, c, d = str(a), str(b), str(c), str(d)

raiz=None
raiz=insertar_nodo(raiz,a)
raiz=insertar_nodo(raiz,b)
raiz=insertar_nodo(raiz,c)
raiz=insertar_nodo(raiz,d)
