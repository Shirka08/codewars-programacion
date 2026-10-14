def permute_a_palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")
    lista1 = []

    for letra in string:
        if letra in lista1:
            lista1.remove(letra)
        else:
            lista1.append(letra)

    return len(lista1) <= 1