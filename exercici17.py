def sumar_llista(a):
    suma = 0
    for i in a:
        suma += i
    return suma

def multiplicar_llista(a):
    multiplicar = 1
    for i in a:
        multiplicar *= i
    return multiplicar

# Uso de las funciones:
x = [3, 4, 5, 7]
print("La suma de todos los elementos de la lista es:", sumar_llista(x))
print("La multiplicación de todos los elementos de la lista es:", multiplicar_llista(x))
