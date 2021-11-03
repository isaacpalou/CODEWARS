def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    lista_final = []
    for elemento in array1:
        lista_final.append(elemento * elemento)
    return sorted(lista_final) == sorted(array2)
