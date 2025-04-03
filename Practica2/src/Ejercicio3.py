def buscarFrase(rules:list):
    aux = ''
    palabra_clave = input('Ingrese una palabra clave para buscar: ').lower()
    for elem in rules:
        if palabra_clave in elem:
            aux += elem +'\n'
    return aux