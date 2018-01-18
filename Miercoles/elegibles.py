
mayores = ["Pedro", "Pablo", "Belem", "Luis", "Anahi","Hugo"]
sancionados = ["Hugo", "Paco", "Luis"]

'''
elegibles = list(set(mayores) - set(sancionados))
print(elegibles)
'''


for persona in mayores:
    if not (persona in sancionados):
        print(persona)
