def suma(num1, num2):
    try:
        resultado = float(num1) + float(num2)
        return resultado
    except TypeError:
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


from ast import main
import sys

print('\033[1m''\033[96m'"EJERCICIO 1" '\033[96m''\033[0m')
x=7
y=0

def error_1(x,y):
    #Uso de try and except para controlar las excepciones
    
    try:
        x/y#se evalua la division


    except: #Controlamos que el denominador no sea 0 mediante ZeroDivisionError que permite que el programa lo dectecte
        raise ZeroDivisionError("Dividir entre 0 no es posible") #cuando se divide entre cero, el programa lanzara este mensaje. Además de que se guardará el error mediante el file=sys.stderr
        #Al incluir ZeroDivisionError no tenemos porque preocuparnos por añadir el file=sys.stdrr pues estamos utilizando un comando que ya tiene almacena este tipo de error

        sys.exit() #Salimos del try and except


#comprobamos la funcion funciona
print(error_1(x,y))

#importamos a main
if __name__=="__main__":
   main()