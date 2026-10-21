def duplicate_encode(palabra):
    palabra = palabra.lower()  #la convierte en minusculas
    resultado = ""     #Crea una lista a la que le vas añadiendo cosas

    for letra in palabra:           #Crea la variable letra dentro de palabra, es un bucle 
        if palabra.count(letra) == 1 :     #la letra solo aparece una vez
            resultado += "("
        else:                                 #la letra aparece mas de una vez
            resultado += ")"

    return resultado