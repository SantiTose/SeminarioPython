import string
def verificarSiSonAnagramas(pal1:str,pal2:str):
    es = 'No es un anagrama!'
    if (sorted(pal1.lower())== sorted(pal2[::-1].lower())):
        es = 'Es un anagrama!'
    return es