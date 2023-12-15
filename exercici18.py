def invertir (cadena):
    #Aquesta funció el que fa es passar la cadena creada a invertirla
    return cadena [::-1]
#Aqui el que feim es crear una cadena la qual el que passara es retornar-la invertida
cadena_normal = "Soy de mi mamá"
#Aqui li posa el mateix avalor perque impriesqui la llista invertida.
cadena_invertida = invertir(cadena_normal)
#Aqui la imprimeix
print(cadena_invertida)