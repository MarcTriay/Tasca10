def crear_llista_fitxer(fitxer):
    # Obre el fitxer en mode de lectura ('r')
    with open(fitxer, 'r') as f:
        # Llegeix totes les línies del fitxer
        llista = f.readlines()

    # Elimina els caràcters de nova línia ('\n') de cada línia
    lparaules = [linea.rstrip('\n') for linea in llista]
    
    # Imprimeix 
    print(lparaules)

# Principal
# Crida la funció 
crear_llista_fitxer('/home/professorat/AO/prova.txt')

