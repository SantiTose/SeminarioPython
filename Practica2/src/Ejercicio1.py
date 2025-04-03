def vocalSegundaPalabra(zen:list):
    vocales = ("a","e","i","o","u")
    aux = ""
    for frase in zen:
        palabras = frase.split()
        if (palabras[1].lower().startswith(vocales)):
            aux+= frase + '\n'
    return aux