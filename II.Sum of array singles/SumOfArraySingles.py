def repeats(arr):
    lista = []
    for elemento in arr:
        if (arr.count(elemento)) < 2:
            lista.append(elemento)
        else:
            continue
    return lista[0] + lista[1]
