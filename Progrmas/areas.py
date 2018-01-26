import os
import math

"""

Programa que calcula el area de 4 diferentes figuras geometricas

"""

def menu():

	"""

	Función que limpia la pantalla y muestra nuevamente el menu

	"""

	os.system('clear') # NOTA para windows tienes que cambiar clear por cls

	print ("Selecciona una opción")

	print ("\t1 - Cuadrado ")

	print ("\t2 - Rectangulo")

	print ("\t3 - Triangulo")

	print ("\t4 - Circulo")

	print ("\t5 - Salir")


while True:

	# Mostramos el menu

	menu()



	# solicituamos una opción al usuario

	opcionMenu = input("¿Que area desea calcular?")




	if opcionMenu=="1": #Calcula el area de un Cuadrado


		lado = float (input("Introduce el lado : "))
		area_cuadrado = lado * lado
		print(area_cuadrado)

		input("Has pulsado la opción 1...\npulsa una tecla para continuar")

	elif opcionMenu=="2": #Calcula el area de un Rectangulo
		base = float (input("Introduce una base : "))

		altura = float (input("Introduce una altura : "))

		area_rectangulo = base * altura

		print (area_rectangulo)

		input("Has pulsado la opción 2...\npulsa una tecla para continuar")

	elif opcionMenu=="3": #Calcula el area de un Triangulo

		base_triangulo = float (input("Introduce una base : "))

		altura_triangulo = float (input("Introduce una altura : "))

		area_triangulo = (base_triangulo * altura_triangulo)/2

		print (area_triangulo)

		input("Has pulsado la opción 3...\npulsa una tecla para continuar")

	elif opcionMenu=="4": #Calcula el area de un Circulo

		radio = float (input("Introduce el radio : "))

		area_circulo = (math.pi * (radio * radio))

		print (area_circulo)

		input("Has pulsado la opción 4...\npulsa una tecla para continuar")

	elif opcionMenu=="5":

		break

	else:

		print ("Error")

		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
