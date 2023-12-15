# Función para mostrar una cuenta regresiva desde i hasta 1
def mostrar(i):
    b = []  
    for e in range(i, 0, -1):  
        b.append(e)  
    print(' '.join(map(str, b)))  

# Parte principal del programa
x = int(input("Introduce un número pequeño: "))  
for i in range(x, 0, -1):  
    mostrar(i) 



