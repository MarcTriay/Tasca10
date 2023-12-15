def crear_punts(llista):
    for num in llista:
        #Aqui la imprimex
        print("." * num)

def dibuixar_imatge(imatge):
    for linia in imatge:
        crear_punts(linia)

#Ceram la imatge cada nombre es una columna la qual tindra els punts que hagui possat es a dir si hi ha 4 hi ha 4 punts
imatge_a_dibujar = [
    [7, 3, 4, 3, 7],
    [5, 6, 5],
    [7, 6, 8, 2, 5],
    [4, 3, 1, 2, 6, 3, 7]
]

dibuixar_imatge(imatge_a_dibujar)