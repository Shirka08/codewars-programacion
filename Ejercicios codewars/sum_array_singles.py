def repeats(numbers):
    unicos = []

    for numero in numbers:
        if numbers.count(numero) == 1:
            unicos.append(numero)
            
    return sum(unicos)