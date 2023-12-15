
def es_vocal(c):
    #Cream aquesta llista que determina si es vocal o no
    return c.lower() in ['a', 'e', 'i', 'o', 'u']
# Ús de la funció, la qual el que fa es fer que possi un lletra i et dira si es vocal o no
lletra = input('Introdueixi una lletra per a veure si és vocal o no: ')
if es_vocal(lletra):
    #Si es es alguna de la llista de la definició es vocal sera vocal, sino(else no ho serà)
    print('És vocal!')
else:
    print('No és vocal!')
