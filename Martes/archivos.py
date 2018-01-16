'''
Archivos
'''
#Como leer arechivos
archivo = open("prueba.txt" , "w")
archivo.write("renglon 1 \n")
archivo.write("renglon 2 \n")
archivo.write("renglon 3 \n")
archivo.close()

#Como escribir archivos

archivo = open ("nombres.txt", "r")
#texto = archivo.read()
for renglon in archivo:
    print(renglon)
