def es_palindrom(palabra):
    #Convertim tots els caràcters minúscules per considerar la majúscula i minúscules equivalents.
    palabra = palabra.lower()
    return palabra == palabra[::-1]

#Exemples:
print(es_palindrom("messi"))   
print(es_palindrom("fuerza"))     
print(es_palindrom("puerta"))  
print(es_palindrom("vaca"))  
print(es_palindrom("scar"))   
print(es_palindrom("arbol"))   
print(es_palindrom("sniper")) 