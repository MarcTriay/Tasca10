def es_palindrom(palabra):
    #Convertimos todas los carácteres minúsculas para considerar la mayúscula y minúsculas equivalentes.
    palabra = palabra.lower()
    return palabra == palabra[::-1]

#Ejmplos de uso.
print(es_palindrom("messi"))   
print(es_palindrom("fuerza"))     
print(es_palindrom("puerta"))  
print(es_palindrom("vaca"))  
print(es_palindrom("scar"))   
print(es_palindrom("arbol"))   
print(es_palindrom("sniper")) 