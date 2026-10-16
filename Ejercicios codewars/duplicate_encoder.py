def duplicate_encode(palabra):
    palabra = palabra.lower()  #la convierte en minusculas
    resultado = ""

    for letra in palabra:
        if palabra.count(letra) == 1 :     #la letra solo aparece una vez
            resultado += "("
        else:                                 #la letra aparece mas de una vez
            resultado += ")"

    return resultado