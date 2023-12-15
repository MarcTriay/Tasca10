suma=0
#Intrdueixes el numero que vulguis
a = input("Introdueix un número: ")
print("{} té {} dígits".format(a,len(a)))
#calculem la si el numero es parell o senar i depengent de el que sigui l'imprimiren d'aguna forma
for i,e in enumerate(a):
    if i%2==0:
        print("El número parell {} és {}".format(i,e))
