 #Crearem variables
a = [2, 3, 4]
b = [2, 5, 8]
a += b # esto es igual a "a = a + b"
print(a)


"""
a = [3, (1,3), [4, 5, 6], 7, "hola", "0", 0, 1]
if "a" in a:
    print("a és dins la llista {}".format(a))
elif "holas" in a:
    print("hola és dins la llista {}".format)

def intercanvi(a, b):
    return b,a
"""

#Modificam la lllista
"""def canvi(l):
    x= int(input("Intro sw posició a canviar: "))#Nosaltres posam un nombre aleatori
    l[x] =int(input("Introdueix el valor a inserir: "))#Aqui decidim a quina posció ho feim
#Programa principal
a=[3, 4, 5, 6 ,7, 8, "a", (1,2),[3,4],10]#Aqui la llista es crea 
print("El valor de la llista abans de canviar és: {}".format(a))##Aqui retorna la llista a
canvi(a)
print("EL valor de la llista despres de canviar és: {}".format(a))#I aqui la retorna
"""
"""def canvi(l):
    x=int(input("Introdueix el valor inserit al conjunt: "))
    l.add(x)

#Programa principal
a={3, 5, 6, 7, 8, 10}
print("El valor de la tupla de abans de caviar era: {}".format(a))
canvi(a)
print("El valor d'ara es: {}".format(a))"""


"""
def canvi(l):
    x=int(input("Introdueix el valor inserit al conjunt: "))
    l[x]=int(input("Introdueix un nou valor per aquetsa clau: "))
a={"a":3,"b": 5,"c": 6,"d": 7,"e": 8,"f": 10}
print("El valor de la tupla de abans de caviar era: {}".format(a))
canvi(a)
print("El valor d'ara es: {}".format(a))
"""
def canvi(l,m,n):
    print("{}{} \n {}".format(l, m, n))
    l="adeu, "
    