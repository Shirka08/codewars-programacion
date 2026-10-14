def to_camel_case(text):
    text = text.replace("_", "-")

    while "-" in text:
        posicion = text.find("-")
        letra = text[posicion + 1].upper()
        text = text.replace(text[posicion:posicion + 2], letra, 1)