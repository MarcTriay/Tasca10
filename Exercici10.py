#Definició de la funció, el que feim es que com el progrma
def major(a):
        #El que feim aqui es depenent de la edad posada posam un if persi te +18 en aquest cas posariam imprimint que es major de edad, 
        if a > 18:
         print("La persona es mayor de edad")
        elif a< 18:
          #AQui el elif posam que si es <18 imprimiriam es menor
          print("Es menor de edad")
        else:
             #I amb un else com ultima opció posarem que te 18 anys ja que si no es major o menor te que ser el 18
             print("Té 18 anys, es a dir es major de edad")

#Programa principal, el que feim aqui es que la persona que utilitzi el programa digui la seva edad amb un int(input, ja que ho vegui i pugui implementar la seva edad o una aleatoria )
x = int(input("Ingrese la edad de la persona "))
major (x)