def find_word(num_let, max_ssw):
    Palabra_Final = None           #Se crea la variable con None porque aun no hay palabra
    Puntuacion_Final = -1          #Se guarda la mejor puntuacion en una variable, se pone -1 porque aun no hay puntuacion

    for palabra in WORD_LIST:      #Por cada palabra en la lista que nos han dado
        if len(palabra) == num_let:   #Si el numero de letras de la palabra es igual a el numero de letras que nos piden
            puntuacion = 0        #Para la puntuacion de la palabra

            for letra in set(palabra):       #Por cada letra dentro de la palabra
                puntuacion += ord(letra) * palabra.count(letra)        #Se añade a la puntuacion; puntuacion de la letra * cada vez que aparece

            if puntuacion <= max_ssw:   #La puntuacion tiene que ser menor o igual que el maximo que nos dan

                if puntuacion > Puntuacion_Final:    #Si la puntuacion es mayor que la que hay en la variable de puntuacion final
                    Puntuacion_Final = puntuacion    #Sustituye la puntuacion que habia por la actual
                    Palabra_Final = palabra          #Cambia la palabra

                elif puntuacion == Puntuacion_Final:   #Cuando dos palabras tienen la misma puntuacion
                    if palabra > Palabra_Final:       #Compara cual es la mayor alfabeticamente
                        Palabra_Final = palabra       #Sustituye

    return Palabra_Final