import string
def comprobarUsuario(nombre:str):
    mayus = tuple(string.ascii_uppercase)
    minus = tuple(string.ascii_lowercase)
    num = tuple(string.digits)
    cara = tuple(string.punctuation)
    uno = False
    dos = False
    if (len(nombre) >= 5):
        for car in nombre:
            if not(car in cara):
                if not uno and (car in mayus):
                    uno = True
                elif not dos and (car in num):
                    dos = True
            else:
                uno,dos = False,False
                break
    if uno and dos:
        print('Nombre de usuario valido')
    else:
        print('Nombre de usuario invalido')