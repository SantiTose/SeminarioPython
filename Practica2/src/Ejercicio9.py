import string
def arreglar(dato:str):
    datoarreglado = None
    if dato != None and len(dato) > 5: 
        dato = dato.split()
        datoarreglado = f'{dato[0].title()} {dato[1].title()}'
    return datoarreglado
    
        
def arreglarDatos(lista:list):
    listaarreglada = []
    for elem in lista:
        elem = arreglar(elem)
        if elem != None:
            listaarreglada.append(elem)
        for elem in listaarreglada:
            cant = listaarreglada.count(elem)
            if cant > 1:
                for i in range(cant-1):
                    print(f'Encontre uno {i}')
                    pos = listaarreglada.index(elem)
                    listaarreglada.pop(pos)
    return listaarreglada
