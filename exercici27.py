def mayusculas(lista):
    #Feim que es alegeixen les paraules amb mayuscula
    result = []
    for palabra in lista:
        if any(char.isupper() for char in palabra):
            result.append(palabra)
    return result
#FEim que introdueixi una serie de paraules
lista = input("Ingrese una lista de palabras separadas por comas: ").split(',')
#Las conjunta
resultado = mayusculas(lista)
#LA imprimim
print("Las palabras que contienen una mayúscula son:", resultado)