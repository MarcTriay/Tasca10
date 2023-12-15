def gran(a, b, c):
    #Cream una definició la qual el que farem es passar el numero per aqui i nos decidirà si es major, menor, igual
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

# Uso de la función, aqui feim que es pugui introduir el numero amb una lletra per despres passar-ho a la funció
x = int(input("Introduce el primer número a comparar: "))
y = int(input("Introduce el segundo número a comparar: "))
z = int(input("Introduce el tercer número a comparar: "))
resultado = gran(x, y, z)
print("El número más grande es:", resultado)
