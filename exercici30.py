def mostrar_majors_que(tupla, referencia):
    majors = [num for num in tupla if num > referencia]
    print(f"Nombres majors que {referencia}: {majors}")

def nums_que_comencen_per(llista_noms, lletra):
    noms_comencen_a = [nom for nom in llista_noms if nom.startswith(lletra)]
    return len(noms_comencen_a)

def main():
    # Funció mostrar_majors_que
    tupla = tuple(map(int, input("Introdueix els valors de la tupla separats per espai: ").split()))
    referencia = int(input("Introdueix la referència per comparar: "))
    mostrar_majors_que(tupla, referencia)

    # Funció nums_que_comencen_per
    noms = input("Introdueix els noms separats per espai: ").split()
    lletra_a = 'a'
    quantitat_noms_a = nums_que_comencen_per(noms, lletra_a)
    print(f"Hi ha {quantitat_noms_a} noms que comencen amb la lletra 'a'.")

if __name__ == "__main__":
    main()
