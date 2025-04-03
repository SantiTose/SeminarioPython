def agregarKeys(jugador:dict):
    jugador =  {'Kills': 0,"Asistencias": 0,"Muertes": 0,"Mvps":0,"Puntos":0}
    return jugador

def procesarJugador(jug:dict,ronda:dict,total:dict,mvp:dict):
    kills = ronda[jug]["kills"]
    asistencias = ronda[jug]["assists"]
    muerte = ronda[jug]["deaths"]
    puntos = kills*3 + asistencias
    if muerte:
        puntos -= 1
        total[jug]["Muertes"]+= 1
    total[jug]["Kills"] += kills
    total[jug]["Asistencias"] += asistencias
    total[jug]["Puntos"]+= puntos
    if(mvp['puntos']<puntos):
        mvp['nombre'] = jug
        mvp['puntos']= puntos
    
def imprimirRonda(ronda:dict):
    print('-'*56)
    print(f'| Jugador {''*3} Kills {''*3} Asistencias {''*3} Muertes {''*3} MVPs {''*3} Puntos   |')
    for jug in ronda:
        nombre = f"{jug}".center(8)
        kills = f"{ronda[jug]["Kills"]}".center(7)
        asistencias = f"{ronda[jug]["Asistencias"]}".center(8)
        muertes = f"{ronda[jug]["Muertes"]}".center(12)
        mvps = f"{ronda[jug]["Mvps"]}".center(0)
        puntos = f"{ronda[jug]["Puntos"]}".center(11)
        print('|',nombre,kills,asistencias,muertes,mvps,puntos,'|')
    print(''*56)

def procesarPartida(rondas:list):
    total = {}
    for i,ronda in enumerate(rondas):
        mvp = {'nombre': '',"puntos": 0}
        for jug in ronda:
            if jug not in total:
                total[jug] = agregarKeys(total) # Solo uso esta funcion en la primera ronda
            procesarJugador(jug,ronda,total,mvp)
        quienfue = mvp['nombre']
        total[quienfue]["Mvps"] +=1
        total = dict(sorted(total.items(), key = lambda x: x[1]["Puntos"], reverse=True))
        # Items me combierte a total que es un diccionario, a una tupla en la que cada elemento contiene un 
        # diccionario con clave como el nombre del jugador y valor como las estadisticas de este, esto me
        # ayuda a que con una lambda acceder a la posicion puntos de cada jugador
        print(f'Resultado de la Ronda {i+1}')
        imprimirRonda(total)
    print('Ranking Final')
    imprimirRonda(total)
    return 'Juego Finalizado'