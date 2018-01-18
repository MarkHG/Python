'''
Dados tres numeros impares te imprima el mayor impar
'''

a = int (input("dame el valor de a: "))
b = int (input("dame el valor de b: "))
c = int (input("dame el valor de c: "))

if (a > b and a % 2 != 0 and b % 2 != 0 and c % 2 != 0):
    print(a)
elif (c > b and c % 2 != 0 and a % 2 != 0 and b % 2 != 0):
    print(c)
elif (b > a and b > c and b % 2 != 0 and a % 2 != 0 and c % 2 != 0):
    print(b)
else:
    print("Algun numero que ingresaste no es impar")
