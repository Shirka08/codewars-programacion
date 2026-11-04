def merge(*diccionarios):                                #El * recoge los argumentos en una tupla
    resultado = { }                                      #Creo un diccionario
    for diccionario in diccionarios:                     #Para cada diccionario dentro de todos los que me dan
        for letra, numero in diccionario.items():         #Para cada letra y numero que hay dentro del diccionario
            if letra in resultado:                       #Si la letra esta dentro del diccionario
                resultado[letra].append(numero)           #Le añades solo el numero
            else:                                        #Si no esta
                resultado[letra]= [numero]                #Le añades la letra y el numero
    return resultado 