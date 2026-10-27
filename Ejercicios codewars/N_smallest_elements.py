def first_n_smallest(arr, n):
    original = arr.copy()
    resultado = []
    contador = 0

    while contador < n:
        menor = min(arr)
        resultado.append(menor)
        arr.remove(menor)
        contador += 1

    lista_final = []

    for numero in original:
        if numero in resultado:
            lista_final.append(numero)
            resultado.remove(numero)

    return lista_final