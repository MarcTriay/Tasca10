def bintodec(num):
    #Calcula el numero en binari i ho passa a enter
    return int(num,2)
#Feim que una introduesqui un numero en binari
num = input("Introdueix un número en binari: ")
a = bintodec(num)
#Imprimeix el resultat
print("Numero binari {}  passat a enter {}".format(num,a))