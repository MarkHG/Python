import random #Biblioteca que genera un numero aleatorio de 0.0 - 1.0
import math

a = int (random.random() * 10) #Genera numeros aleatorios del 1 al 10
print(a)

b = random.randint(0,500) # Genera numero aleatorios del 0-500
print(b)

print(math.pi)
print(math.e)
print(math.sin(14))
print(math.tan(20))


a = int (input("dame el valor de a: "))
b = int (input("dame el valor de b: "))
c = int (input("dame el valor de c: "))

d = b * b - 4 * a * c
print(d)

'''
if (d > 0):
    print("¡Raíces reales y diferentes!")
elif (d = 0):
    print("¡Raíces reales e iguales!")
elif (d < 0)
    print("¡Raíces complejas conjugadas!)
else:
    print("")
'''


x1 = - b + math.sqrt(d)
print(x1/2*a)

x2 = - b - math.sqrt(d)
print(x2/2*a)
