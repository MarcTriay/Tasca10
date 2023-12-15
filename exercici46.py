# Funció per verificar si una llista està ordenada
def esta_ordenada(a):
    b = a.copy()
    a.sort()
    if a == b:
        print("La llista {} està ordenada {}".format(a, b))
    else:
        print("La llista {} no està ordenada {}".format(a, b))

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
if __name__ == "__main__":
    # Llegir la llista
    a = llegir_llista()

    # Ordenar la llista abans de comprovar si està ordenada
    a.sort()

    # Comprovar si la llista està ordenada
    esta_ordenada(a)

