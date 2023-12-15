# Funció per verificar si hi ha elements duplicats en una llista
def hi_ha_duplicats(a):
    seen = set()  # Conjunt per emmagatzemar els elements que ja s'han vist
    dupes = set(x for x in a if x in seen or seen.add(x))  
    if len(dupes) > 0:
        print("La llista {} té elements duplicats {}".format(a, dupes))
    else:
        print("La llista {} no té elements duplicats".format(a))

# Funció per llegir una llista d'elements fins que es introdueix un punt (.)
def llegir_llista():
    a = []         
    c = "a"
    while c != ".":
        c = input("Introdueixi un element de la llista i punt (.) per acabar: ")
        if c != ".":
            a.append(c)  
    return a

# Principal
a = llegir_llista()  # Crida a la funció per llegir la llista
hi_ha_duplicats(a)   # Crida a la funció per verificar si hi ha elements duplicats
