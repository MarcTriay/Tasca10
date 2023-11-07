#Passat el menú ara hi ha que añadir les operacions if, else, elif

def calculadora_enters ():
    op = 1
    while op>0:
        print("""
            Menu_principal:
                1. Sumar
                2. Resta
                3. Divició
                4. Multiplicar
                5. Sortida
              """)
        
        op = int(input("Elige la opción: "))
        match op:
            case 1:
                a = int(input("Introdueix un nombre: "))
                b = int(input("Introdueix el segon nombre per sumar: "))
                print("La suma de {} + {} = {}".format(a,b,a+b))

            case 2:
                a = int(input("Introdueix un nombre: "))
                b = int(input("Introdueix el segon nombre per restar: "))
                print("La resta de {} + {} = {}".format(a,b,a-b))

            case 3:
                a = int(input("Introdueix un nombre: "))
                b = int(input("Introdueix el segon nombre per multiplicar: "))
                print("La multiplicació de {} + {} = {}".format(a,b,a*b))

            case 4:
                a = int(input("Introdueix un nombre: "))
                b = int(input("Introdueix el segon nombre per dividir: "))
                print("La divició de {} + {} = {}".format(a,b,a/b))
            case 5:
                op = -1




def calculadora_reals ():
    z = 1
    while z>0:
        print("""
            Menu_principal:
                  1. Sumar
                  2. Resta
                 3. Divició
                 4. Multiplicar
                  5. Sortida
                 """)
        z = int(input("Elegeix una opció: "))
        match z:
            case 1:
                a = float(input("Introdueix un nombre: "))
                b = float(input("Introdueix el segon nombre per sumar: "))
                print("La suma de {} + {} = {}".format(a,b,a+b))

            case 2:
                a = float(input("Introdueix un nombre: "))
                b = float(input("Introdueix el segon nombre per restar: "))
                print("La resta de {} - {} = {}".format(a,b,a-b))

            case 3:
                a = float(input("Introdueix un nombre: "))
                b = float(input("Introdueix el segon nombre per multiplicar: "))
                print("La multiplicació de {} * {} = {}".format(a,b,a*b))

            case 4:
                a = float(input("Introdueix un nombre: "))
                b = float(input("Introdueix el segon nombre per dividir: "))
                print("La divició de {} / {} = {}".format(a,b,a/b))
            case 5:
                z =-1

def menu_principal():
    b = 1
    while b>0:
        print("""
            Menu_principal:
                1. Calculadora enteros
                2. Calculadora reales
                3. salida
            """)
        b = int(input("Elige la opción: "))
        if b>0 and b<4:
            return b
        else:
            print("Opció no vàlida, torni a indicar la seva selecció: \n")


#Programa principal
opcio = 1
while opcio>0:
    opcio = menu_principal() 
    match opcio:
        case 1:
            calculadora_enters()
        case 2:
            calculadora_reals()    
        case 3:
            print("Gracies per utiliçar el programa")
            opcio = -1
