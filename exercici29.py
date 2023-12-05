from datetime import datetime

def calcular_anys_naixement(any_actual, any_naixement):
    return any_actual - any_naixement

def imprimir_dades(noms, dates_naixement, any_actual):
    print("Nom\t\tData naixement\tAnys que farà aquest any")
    for i in range(len(noms)):
        anys = calcular_anys_naixement(any_actual, dates_naixement[i])
        print(f"{noms[i]}\t\t{dates_naixement[i]}\t\t{anys}")

def main():
    any_actual = int(input("Introdueix l'any actual: "))
    
    noms = []
    dates_naixement = []

    for i in range(4):
        nom = input(f"Introdueix el nom de la persona {i + 1}: ")
        data_naixement = int(input(f"Introdueix l'any de naixement de {nom}: "))
        noms.append(nom)
        dates_naixement.append(data_naixement)

    imprimir_dades(noms, dates_naixement, any_actual)

if __name__ == "__main__":
    main()
