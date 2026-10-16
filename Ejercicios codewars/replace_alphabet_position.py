def alphabet_position(text):
    resultado = ""

    for letra in text.lower():       #Para una letra de la palabra en minusculas
        if letra.isalpha():           #si ea letra es una letra y no un simbolo
            numero = ord(letra) - 96   #Combierte la letra en un numero
            resultado += str(numero) + " "   # Suma los numeros con un espacio en medio
             
    return resultado.strip()    #elimina el ultimo espacio