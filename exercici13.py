def numero_mayor():
    a = int(input("Introduce un numero: "))
    b = int(input("Introduce un numero: "))
    if a>b:
        print("El número major {} i {} és {}".format(a, b, a))
    elif b>a:
        print("El número major {} i {} és {}".format(a, b, b))
    else:
        print("El números són iguals {} i {}".format(a, b))

def menu():
    print("1. Comparar números")
    print("2. Salir")
    return int(input("Introduce una opción: "))

#Programa principal
opcio = 1
while opcio>0:
    opcio = menu()
    match opcio:
        case 1:
            numero_mayor()
        case 2:
            opcio=-1
        case other:
            print("Opció no vàlida")