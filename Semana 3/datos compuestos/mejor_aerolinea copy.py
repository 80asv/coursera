def mejor_aerolinea(vuelos:dict)->str:
    mejor=""
    mejor_promedio=100000000
    retraso_acum={}
    retraso_cuantas={}
    for vuelo in vuelos:
        info_vuelo=vuelos[vuelo]
        retraso=info_vuelo["retraso"]
        aerolinea=info_vuelo["aerolinea"]

        retraso_acum[aerolinea]=retraso_acum.get(aerolinea,0)+retraso
        retraso_cuantas[aerolinea]=retraso_cuantas.get(aerolinea,0)+1

        if retraso_acum[aerolinea]/retraso_cuantas[aerolinea] < mejor_promedio:
            mejor=aerolinea
            mejor_promedio=retraso_acum[aerolinea]/retraso_cuantas[aerolinea]
            
    return mejor

d1 = {
    "001": {
        "aerolinea": "despegar",
        "origen": "colombia",
        "destino": "paris",
        "retraso": 3556810
    },
    "002": {
        "aerolinea": "despegar",
        "origen": "colombia",
        "destino": "paris",
        "retraso": 3850
    },
    "003": {
        "aerolinea": "felipe",
        "origen": "colombia",
        "destino": "paris",
        "retraso": 350
    },
    "004": {
        "aerolinea": "andres",
        "origen": "colombia",
        "destino": "paris",
        "retraso": 30
    }
}



r = mejor_aerolinea(d1)

print(r)