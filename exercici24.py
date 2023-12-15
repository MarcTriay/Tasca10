def gran_lista(l):
    # El que fa es agafar el número més gros
    if not l:
        return None
    max = l[0]
    for n in l:
        if n > max:
            max = n
    return max
#Crem la llista
l = [3, 4, 2, 3, 10]
r = gran_lista(l)
print(r)