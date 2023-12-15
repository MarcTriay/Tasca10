suma=0
#Feim que introdeusqui un numero
a = input("Introdueix un número: ")
print("{} té {} dígits".format(a,len(a)))
for i in a:
	suma = suma + int(i)
	#Imprimim resultat
print("La suma dels dígits del número {} és {}".format(a,suma))
if suma%2==0:
	#calculam si la funció es parell o es senar
	print("La suma dels dígits del número {} és parell".format(a))
else:
	print("La suma dels dígits del número {} és senar".format(a))
