def spin_words(frase):
    palabras = frase.split()
    frase_completa = []
    for palabra in palabras:
        if len(palabra) > 4: 
            reves = palabra [::-1]
            frase_completa.append(reves)
        else:
             frase_completa.append(palabra)
            
            
    return  " ".join(frase_completa)