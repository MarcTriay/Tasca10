def numero_mayor():
    a = int(input("Introduce un numero "))
    b = int(input("Introduce un numero"))
    return a>b or a==b and b>0 or b>a and a>0

def menu():
    print("1. Comparar números")
    print("0. Salir")
    return int(input("Introduce una opción: "))

def main():
    while True:
        opcio = menu()
        if opcio == 0:
            break
        elif opcio == 1:
            a = int(input("Introduce un numero "))
            b = int(input("Introduce un numero"))
            if numero_mayor(a, b):
                print(f"{a} Es el mayor que {b}")
            elif numero_mayor(b, a):
                print(f"{b} Es el mayor que {a}")
            else:
                print("Los dos numeros son iguals")

