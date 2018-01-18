'''
Clase Libro
'''
import statistics

class Libro:
    titulo = ""
    autor = ""
    precio = 0

    def __init__(self,titulo,autor,precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

libros = []
archivo = open("libros.csv", "r")

for renglon in archivo:
        registro = renglon.split(",")
        libros.append(Libro(registro[0],registro[1],int(registro[2][:-1])))
archivo.close()
for o in libros:
    print(o.titulo)

datos = []
for objeto in libros:
    datos.append(objeto.precio)
print(statistics.mean(datos))
