class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.memo = {}
        self.izq = None
        self.der = None

    def sumar(self, otro):
        if otro is None:
            return self
        if (self, otro) in self.memo:
            return self.memo[(self, otro)]
        resultado = Nodo(self.valor + otro.valor)
        resultado.izq = self.izq.sumar(otro.izq)
        resultado.der = self.der.sumar(otro.der)
        self.memo[(self, otro)] = resultado
        return resultado

    def restar(self, otro):
        if otro is None:
            return self
        if (self, otro) in self.memo:
            return self.memo[(self, otro)]
        resultado = Nodo(self.valor - otro.valor)
        resultado.izq = self.izq.restar(otro.izq)
        resultado.der = self.der.restar(otro.der)
        self.memo[(self, otro)] = resultado
        return resultado

    def multiplicar(self, otro):
        if otro is None:
            return self
        if (self, otro) in self.memo:
            return self.memo[(self, otro)]
        resultado = Nodo(self.valor * otro.valor)
        resultado.izq = self.izq.multiplicar(otro.izq)
        resultado.der = self.der.multiplicar(otro.der)
        self.memo[(self, otro)] = resultado
        return resultado

    def dividir(self, otro):
        if otro is None:
            return self
        if (self, otro) in self.memo:
            return self.memo[(self, otro)]
        if otro.valor == 0:
            print("No se puede dividir entre cero.")
            return None
        resultado = Nodo(self.valor / otro.valor)
        resultado.izq = self.izq.dividir(otro.izq)
        resultado.der = self.der.dividir(otro.der)
        self.memo[(self, otro)] = resultado
        return resultado

arbol1 = Nodo(5)
arbol1.izq = Nodo(2)
arbol1.der = Nodo(7)

arbol2 = Nodo(3)
arbol2.izq = Nodo(8)
arbol2.der = Nodo(4)

resultado = arbol1.sumar(arbol2)
print(resultado.valor)  # 5 + 3 = 8

resultado = arbol1.multiplicar(arbol2)
print(resultado.valor)  # 5 * 3 = 15



