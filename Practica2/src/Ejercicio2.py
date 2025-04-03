def buscarMasPalabras(titles:list):
    max = ''
    for elem in titles:
        if len(elem.split())>len(max.split()):
            max = elem
    return max