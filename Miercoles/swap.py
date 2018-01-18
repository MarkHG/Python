'''
a = 3
b = 5

a, b = 3, 5
a, b = b,a
print(a, b)
'''
a = int (input("dame el valor de a: "))
b = int (input("dame el valor de b: "))
c = int (input("dame el valor de c: "))


if (a > b):
    if(b > c):
        print(a,b,c)
    else:
        print(a,c,b)

else:
    if(b > a):
        print(b,a,c)
    else:
        print(b,c,a)

#dados tres numeros te imprima el mayor impar
