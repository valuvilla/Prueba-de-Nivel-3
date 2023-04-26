class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None
    
    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar(valor, self.raiz)
    
    def _agregar(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._agregar(valor, nodo_actual.izquierda)
        elif valor == nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._agregar(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._agregar(valor, nodo_actual.derecha)
    
    def sumar(self):
        return self._sumar(self.raiz)
    
    def _sumar(self, nodo_actual):
        if nodo_actual is None:
            return 0
        else:
            try:
                nodo_actual.valor=int(int(nodo_actual.valor))
                return int(nodo_actual.valor) + self._sumar(nodo_actual.izquierda) + self._sumar(nodo_actual.derecha)
            except (ValueError,TypeError):
                return "VError: Tipo de dato no válido. "


    def restar(self):
        return self._restar(self.raiz)
    
    def _restar(self, nodo_actual):
        if nodo_actual is None:
            return 0
        else:    
            try:
                nodo_actual.valor=int(int(nodo_actual.valor))
                return int(nodo_actual.valor) - self._restar(nodo_actual.izquierda) - self._restar(nodo_actual.derecha)
            except (ValueError,TypeError):
                return "Error: Tipo de dato no válido."

    def multiplicar(self):
        return self._multiplicar(self.raiz)
    
    def _multiplicar(self, nodo_actual):
        if nodo_actual is None:
            return 0
        else:    
            try:
                nodo_actual.valor=int(int(nodo_actual.valor))
                return int(nodo_actual.valor) * self._multiplicar(nodo_actual.izquierda) * self._multiplicar(nodo_actual.derecha)
            except (ValueError,TypeError):
                return "Error: Tipo de dato no válido."

    def dividir(self):
        return self._dividir(self.raiz)
    
    def _dividir(self, nodo_actual):
        if nodo_actual is None:
            return 0
        else:
            # Exception handling
            try:
                resultado=int(nodo_actual.valor) / self._dividir(nodo_actual.izquierda) * self._dividir(nodo_actual.derecha)
                return resultado
            except (TypeError,ValueError):
                print ("Error: Tipo de dato no válido.")
            except ZeroDivisionError:
                print ("Error: No es posible dividir entre cero.")


    

            


arbol_suma=Arbol()
arbol_resta=Arbol()
arbol_multiplicacion=Arbol()
arbol_division=Arbol()


a,b,c,d=(10,5,0,"Hola")
arbol_suma.agregar((a))
arbol_suma.agregar((b))
arbol_resta.agregar(str(b))
arbol_resta.agregar(d)
arbol_multiplicacion.agregar(b)
arbol_multiplicacion.agregar(b)
arbol_division.agregar(a)
arbol_division.agregar(c)



print(arbol_suma.sumar())
print(arbol_resta.restar())
print(arbol_multiplicacion.multiplicar())
(arbol_division.dividir())
    
