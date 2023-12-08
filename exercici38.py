def calcular_capital_final():
    # Demana a l'usuari les dades d'entrada
    while True:
        try:
            capital_inicial = float(input("Introdueix la quantitat a sol·licitar (entre 50000€ i 800000€): "))
            if 50000 <= capital_inicial <= 800000:
                break
            else:
                print("Si us plau, introdueix una quantitat vàlida.")
        except ValueError:
            print("Si us plau, introdueix una quantitat vàlida.")

    while True:
        try:
            interes = float(input("Introdueix l'interès (entre 0.5% i 13%): "))
            if 0.5 <= interes <= 13:
                break
            else:
                print("Si us plau, introdueix un interès vàlid.")
        except ValueError:
            print("Si us plau, introdueix un interès vàlid.")

    while True:
        try:
            anys = int(input("Introdueix el número d'anys (entre 3 i 40): "))
            if 3 <= anys <= 40:
                break
            else:
                print("Si us plau, introdueix un número d'anys vàlid.")
        except ValueError:
            print("Si us plau, introdueix un número d'anys vàlid.")

    # Calcula el capital final utilitzant la fórmula proporcionada
    capital_final = capital_inicial * (1 + interes / 100) ** anys

    # Mostra el resultat
    print(f"El capital final serà: {capital_final:.2f}€")


# Executa la funció per calcular el capital final
calcular_capital_final()
