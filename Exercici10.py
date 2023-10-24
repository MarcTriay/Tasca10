#Definició de la funció
def major(a):
        if a > 18:
         print("La persona es mayor de edad")
        elif a< 18:
          print("Es menor de edad")
        else:
             print("Té 18 anys")

#Programa principal
x = int(input("Ingrese la edad de la persona "))
major (x)