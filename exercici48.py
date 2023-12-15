from random import randint

# Funció per generar una llista de 20 elements aleatoris entre 1 i 100
def llista_20_elements():
    l = []
    for _ in range(20):
        l.append(randint(1, 100))
    return l

# Funció per verificar si hi ha elements duplicats en una llista
def hi_ha_duplicats(a):
    seen = set()  
    dupes = set(x for x in a if x in seen or seen.add(x))  
    if dupes:
        print("La llista {} té elements duplicats {}".format(a, dupes))
    else:
        print("La llista {} no té elements duplicats".format(a))

# Principal
x = llista_20_elements()  
hi_ha_duplicats(x)       
