def nums_que_comencen_per_a(llista_noms):
    noms_comencen_per_a = [nom for nom in llista_noms if nom.lower().startswith('a')]
    return len(noms_comencen_per_a)

# Exemple d'ús
llista_noms = ['Sergi', 'Ayoub', 'Marc', 'Leiner']
quantitat_noms = nums_que_comencen_per_a(llista_noms)
print("{}".format(llista_noms))
print(f"Hi ha {quantitat_noms} noms que comencen per la lletra 'a'.")
