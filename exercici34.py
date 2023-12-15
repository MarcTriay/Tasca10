def es_de_traspas(any):
    #Calcula si l'any introduit és traspas o no
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        return True
    else:
        return False
#Intrrroduex el any
any = int(input("Introdueix un any: "))

if es_de_traspas(any):
    #Ho imprimeix
    print(f"{any} és un any de traspàs.")
else:
    print(f"{any} no és un any de traspàs.")
