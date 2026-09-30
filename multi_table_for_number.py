def multi_table(n):
    table = ""

    for variable in range(1, 11):
        if variable == 10:
            table += f"{variable} * {n} = {variable * n}"
        else:
            table += f"{variable} * {n} = {variable * n}\n"

    return table