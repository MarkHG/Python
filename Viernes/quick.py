import time
import random

'''
Quick Sort
'''
numeros = []
n = 10000
for i in range(n):
    numeros.append(random.randint(0,n))
inicio = time.time()

numeros.sort() # Aqui esta la magia 
fin = time.time()
print(numeros)
print(fin - inicio)
