from preloaded import MORSE_CODE                 # Importa el código Morse

def decode_morse(codigo):  
    frase = []                                   # Crea una lista vacía donde guardaremos los caracteres descodificados
    codigo = codigo.replace("   ", "|")          # Sustituye los tres espacios que separan palabras por |
    palabras = codigo.split("|")                 # Separa el código por donde hay un |

    for palabra in palabras:                     # Recorre cada palabra del código Morse.
        simbolos = palabra.split()               # Separa los códigos Morse individuales de esa palabra.
        for simbolo in simbolos:                 # Recorre cada símbolo Morse.
            frase.append(MORSE_CODE[simbolo])    # Busca su significado Morse y lo añade a la lista.
        frase.append(" ")                        # Añade un espacio para separar las palabras descodificadas.

    resultado = "".join(frase)                   # Une todos los elementos de la lista en una única cadena de texto.
    return resultado.strip()                     # Devuelve el texto final eliminando los espacios sobrantes de los extremos