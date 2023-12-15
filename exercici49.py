import random

# Funció per generar una llista de 20 elements aleatoris entre 1 i 100
def llista_20_elements():
    l = []
    for i in range(20):
        l.append(random.randint(1, 100))
    return l

# Funció per verificar si hi ha elements duplicats en una llista
def hi_ha_duplicats(a):
    seen = set()    
    dupes = [x for x in a if x in seen or seen.add(x)] 	 
    if len(dupes) > 0:
        print("La llista {} té elements duplicats {}".format(a, dupes))
    else:
        print("La llista {} no té elements duplicats {}".format(a, dupes))

# Funció per eliminar duplicats d'una llista
def elimina_duplicats(a):
    b = list(set(a))
    return b

# Principal
x = llista_20_elements()  # Genera una llista de 20 elements aleatoris
hi_ha_duplicats(x)        # Crida a la funció per verificar si hi ha elements duplicats

y = elimina_duplicats(x)  # Elimina duplicats de la llista
y.sort()                  # Ordena la llista sense duplicats
print("Llavors, la llista sense elements duplicats és {}".format(y))
