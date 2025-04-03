import random
import string

def convertirFecha(fecha:str):
    fechaconvertida = ""
    for digito in (fecha):
        if(digito.isdigit()):
            fechaconvertida += digito
    return fechaconvertida
def generarCodigo(nombre:str,fecha:str):
    if(len(nombre) < 15):
        fecha = convertirFecha(fecha)
        resto = 30 - (len(nombre)+len(fecha))
        agregados = string.ascii_uppercase + str(string.digits)
        caracteres = random.choices(agregados,k=resto)
        textoextra = ''
        for car in caracteres:
            textoextra +=car
    return f"{nombre.upper()}-{fecha}-{textoextra}"