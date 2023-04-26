def suma(num1, num2):
    try:
        resultado = float(num1) + float(num2)
        return resultado
    except ValueError:
        print("Error: Tipo de dato no válido")
        return None

def resta(num1, num2):
    try:
        resultado = float(num1) - float(num2)
        return resultado
    except TypeError:
        raise TypeError("Error: Tipo de dato no válido")

def producto(num1, num2):
    try:
        resultado = float(num1) * float(num2)
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido")
        return None

def division(num1, num2):
    try:
        if num2 == 0:
            raise ZeroDivisionError
        resultado = float(num1) / float(num2)
        return resultado
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
        return None
    except TypeError:
        print("Error: Tipo de dato no válido")
        return None

print(resta(1,"Hola"))
    
