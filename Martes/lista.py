'''
Listas en python
'''

a = [7, 5, 1 , 10, 20, 30, 5, 9]

for i in a:
    print (i * 2)
a.sort()
print(a)

b = [1,2,3]

print (b[1:3])
print (b[0:1])

print (a[:: -1])

print(a[0:5:-1])



# Eliminamos palabras repetidas

b = "era una hermosa tarde de invierno hacia frio porque era enero"
c = b.split() #split sepra las palabras
print (c)
d = []
for i in c:
    if not (i in d):
        d.append(i)
d.sort()
print(d)

e = ["hola",7,"buen",3.28,False]
f = ["a",10]
e.append(f)
print(e)
print(e[3])
print(e[-1][1])
print(e[5][1])
