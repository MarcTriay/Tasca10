def comptar_vocals(paraula):
    vocals = "aeiou"
    comptador_vocals = {vocal: 0 for vocal in vocals}

    for lletra in paraula.lower():
        if lletra in vocals:
            comptador_vocals[lletra] += 1

    return comptador_vocals

def main():
    paraula = input("Introdueix una paraula: ")
    resultat = comptar_vocals(paraula)

    for vocal, comptador in resultat.items():
        print(f'Hi ha {comptador} "{vocal}"\'s en la paraula "{paraula.lower()}".')

if __name__ == "__main__":
    main()
