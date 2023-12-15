# Definim la funció superposició
def superposición(lista1, lista2):
    return bool(set(lista1) & set(lista2))
# Iniciam les llistes 'lista_x' i 'lista_z'
lista_x = [6, 7, 8, 9]
lista_z = [777, 69, 6, 50]
#la funció 'superposició' amb les llistes 'lista_x' i 'lista_z'
respuesta = superposición(lista_x, lista_z)
# Impressió del resultat
print(respuesta)