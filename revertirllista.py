a =[2, 3, 4]
print(a)
for i in a:
    b=i*i*i
print(a)
for i in range(len(a)):
    a[i]=a[i]*a[i]*a[i]
print(a)
for i, e in enumerate (a):
    a[i]=e*e*e
print(a)

#Tuples fàcils
def segona_ocurrencial(l,e):
    a = l.count(e)
    if a>1:
        p = l.index(e)
        so =l.index(e,(p+1))
        print (so)
    else:
        print("Nomes hi ha zero o una ocurrència")
    
#Programa principal
l=(1, 4, 2, (1, 3, 3), 3, 4, 2, 1)
x= int(input("Elegeix l'element que vols cercar la 2a ocurrencia "))
segona_ocurrencial(l, x)


