def comp(a, b):
    if a is None or b is None:
        return False

    cuadrados = []

    for numero in a:
        cuadrados.append(numero ** 2)

    cuadrados.sort()
    b.sort()

    return cuadrados == b