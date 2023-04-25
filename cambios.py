import random

numeros= [random.randint(0,100) for _ in range (1,8)]
print(numeros)

numeros_aleatorios = random.sample(numeros,0)

print(numeros_aleatorios)