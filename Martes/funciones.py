'''
Funciones
'''
cont = 10

def triple (algo):
    return algo*3

print(triple(5))
print(triple('hola'))
print(triple(18.49))

def factorial (n):
    if (n == 0):
        return (1)
    else:
        return (n * factorial(n-1))

print(factorial(cont))
print(cont)

a = 3 -4j
b = -2 + 8j

print(a-b)
print(a+b)
print(a*b)
print(a/b)
z = 0 + 1j
print(z ** 2)
