#Introduim els caracters que nescessitam
x = float(input("Introdueixi la quantitat sol·licitada (50000 i 80000) euros: "))
y = float(input("Introdueixi l'interés (0.5 i 13) percentatge: "))
z = int(input("Introdueixi el número d'anys: "))
#Aqui les calculem
cfinal = x * (1 + y/100)**z
#I finalment les impreimim
print("El capital {}€ a un interés del {}% a {} anys resulta que pagarem {:.2f}€".format(x, y, z, cfinal))
