def filtrar_paraules(lista_paraules, x):
    #AQui feim que es seleccioni las paraules que teniguin més carcters i les altres les descarta
    for paraula in lista_paraules:
        if len(paraula) > x:
            print(paraula)
#Introduim una llista
a = input("Introdueix una llistan de paraules separades per espais: ")

paraules = a.split()
#Introduim el numero de caracters minims perque surtin 
x = int(input("Introdueix el mínim de caràcters que tenen que tenir: "))
#Aqui la imprimim
print("Paraules amb més de {} caràcters:".format(x))

filtrar_paraules(paraules, x)