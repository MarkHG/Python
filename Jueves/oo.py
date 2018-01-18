'''
Orientacion a Objetos
'''

class Persona:
    nombre = "" #Variable
    edad = ""
    def __init__(self,nombre,edad): #Metodo constructor
        self.nombre = nombre
        self.edad = edad

    def hablar(self,n): #Metodo
        print("Hey",n)

Persona1 = Persona("Marco","22")
Persona1.nombre = "Marco"
Persona1.edad = "40"
print(Persona1.nombre)
Persona1.hablar("Adrian")
