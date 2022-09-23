


def mejor_aerolinea(vuelos: dict)->str:
    mayor = 0
    promedio_vuelos = 0
    tiempos = {}
    for cod_vuelo in vuelos:
        info_vuelo = vuelos[cod_vuelo]
        promedio_vuelos += info_vuelo["retraso"]
        tiempos[info_vuelo["retraso"]] = info_vuelo["aerolinea"]


    
    return tiempos[min(tiempos.keys())]

    



d1 = {
    "001": {
        "aerolinea": "despegar",
        "origen": "colombia",
        "destino": "paris",
        "retraso": 3556810
    },
    "002": {
        "aerolinea": "babilon",
        "origen": "colombia",
        "destino": "paris",
        "retraso": 3850
    },
    "003": {
        "aerolinea": "andres",
        "origen": "colombia",
        "destino": "paris",
        "retraso": 350
    }
}



r = mejor_aerolinea(d1)

print(r)