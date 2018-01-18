'''
Conjuntos
'''
a = [3,5,7]
a.append(9)

b = [11,13,15]
for elemento in b:
     a.append(elemento)

print(a)

c = [1,2,3]
d = [4,5,6]
c.extend(d)
print(c)
c.insert(2,10) #(Posicion,valor)
print c
c.append(6)
print(c)

e = set(a)
f = set(c)
print(e - f)
print(f - e)
print(e and f)
