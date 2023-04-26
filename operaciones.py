class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.memo = {}

    def sumar(self, otro):
        if (self.valor, otro.valor) in self.memo:
            return self.memo[(self.valor, otro.valor)]
        resultado = Nodo(self.valor + otro.valor)
        self.memo[(self.valor, otro.valor)] = resultado
        return resultado

    def restar(self, otro):
        if (self.valor, otro.valor) in self.memo:
            return self.memo[(self.valor, otro.valor)]
        resultado = Nodo(self.valor - otro.valor)
        self.memo[(self.valor, otro.valor)] = resultado
        return resultado
    
    def multiplicar(self, otro):
        if (self.valor, otro.valor) in self.memo:
            return self.memo[(self.valor, otro.valor)]
        resultado = Nodo(self.valor * otro.valor)
        self.memo[(self.valor, otro.valor)] = resultado
        return resultado
    
    def dividir(self, otro):
        if (self.valor, otro.valor) in self.memo:
            return self.memo[(self.valor, otro.valor)]
        resultado = Nodo(self.valor / otro.valor)
        self.memo[(self.valor, otro.valor)] = resultado
        return resultado


    
    
    def Excepciones(self, otro):
        if (self.valor, otro.valor) in self.memo:
            return self.memo[(self.valor, otro.valor)]
        resultado = Nodo(self.valor ** otro.valor)
        self.memo[(self.valor, otro.valor)] = resultado
        return resultado
