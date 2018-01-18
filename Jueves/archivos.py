'''
Programa que encuentra el nombre el libro del mas caro y su precio
'''

libros = open ("libros.csv" , "r")
mas_caro = 0
for renglon in libros:
    registro = renglon.split(",")
    #print(registro[0]) #Imprime el renglon con el titulo de los libros
    if len(registro) == 3:
        precio = int(registro[2][:-1])
        if (precio > mas_caro):
            mas_caro = precio
            a = registro[0]
            b = registro[2]
print("El libro mas caro es: ")
print(a)
print("Cuyo precio es: ")
print(b)
libros.close()
