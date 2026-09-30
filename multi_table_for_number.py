def multi_table(multiplicando):
    tabla_de_multiplicar = ""

    for multiplicador in range(1, 11):
        if multiplicador == 10:
            tabla_de_multiplicar += f"{multiplicador} * {multiplicando} = {multiplicador * multiplicando}"
        else:
            tabla_de_multiplicar += f"{multiplicador} * {multiplicando} = {multiplicador * multiplicando}\n"

    return tabla_de_multiplicar