# Función para imprimir los elementos en las posiciones pares de una lista
def elements_parells(a):
    for i, e in enumerate(a):
        if i % 2 == 1:
            print(e)

# Función para leer una lista de palabras hasta que se ingrese un punto
def llegir_llista():
    l = []  
    a = 'a'
    while a != '.':
        a = input("Introduce una nueva palabra y punto (.) para terminar: ")
        if a != '.':
            l.append(a)
    return l

# Parte principal del programa
b = llegir_llista()  
elements_parells(b)  
