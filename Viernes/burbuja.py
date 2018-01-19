import time
import random

'''
Algoritmo de ordenamiento burbuja O(n^2)
'''
numeros = []
n = 10000
for i in range(n):
    numeros.append(random.randint(0,n))
inicio = time.time()


for c in range(n):
    for c2 in range(n - (c + 1)):
        if (numeros[c2] > numeros[c2 +1]):
            temp = numeros[c2]
            numeros[c2] = numeros[c2 + 1]
            numeros[c2 + 1] = numeros [c2]

#numeros.sort()
fin = time.time()
print(numeros)
print(fin - inicio)
