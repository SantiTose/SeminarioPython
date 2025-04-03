def contarMenciones(descripcion:list):
    musica = 0
    charla = 0
    entretenimiento = 0
    for frase in descripcion:
        if('música' in frase):
            musica +=1
        elif('charla' in frase):
            charla +=1
        elif('entretenimiento' in frase):
            entretenimiento +=1
    aux =f"Menciones de musica: {musica} \nMenciones de charla: {charla} \nMenciones de Entretenimiento: {entretenimiento}"
    return aux