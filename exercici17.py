#Suma de lista 
def llegir_llista():
    # Anirà llegint elements d'una llista (Aquí enters)
    # Retornarà la llista creada
    a=' '
    l=[]
    while a!='.':
        a = input("Introdueix un nou element de la llista: ")
        if a!=".":
            l.append(int(a)) # Introdueix enters, si vull paraules he de llevar int()
        else:
            return l

def sumar_lista(llista):
    suma = 0
    for valor in llista:
        suma += valor
    return suma 


# Multiplicación lista
def multiplicar_lista(lista):
    producte = 1
    for valor in lista:
        producte *= valor 
    return producte 



#Programa principal
l = llegir_llista()
print("La suma de la llista {} és {}".format(l,sumar_lista(l)))
print("La suma de la llista {} és {}".format(l,multiplicar_lista(l)))
