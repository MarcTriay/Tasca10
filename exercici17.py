def sumar_llista(a):
    #Cream aquesta funció per sumar els valors sumats
    suma = 0
    for i in a:
        suma += i
    return suma

def multiplicar_llista(a):
    #Aqui feim al mateix pero al final el que fa es multiplicar adames de sumar
    multiplicar = 1
    for i in a:
        multiplicar *= i
    return multiplicar

# Aqui li donam els elements necessaria a les definicions ja que li donam una opció de poder possar un nom aleatori.
x = [3, 4, 5, 7]
print("La suma de todos los elementos de la lista es:", sumar_llista(x))
print("La multiplicación de todos los elementos de la lista es:", multiplicar_llista(x))
