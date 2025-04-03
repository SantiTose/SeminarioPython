def clasificarRapidez(velocidad:int):
    if(velocidad <=200):
        return 'Categoria: Rapido'
    elif (velocidad <=500)and (velocidad >200):
        return 'Categoria: Normal'
    elif (velocidad>500):
        return 'Categoria: Lento'