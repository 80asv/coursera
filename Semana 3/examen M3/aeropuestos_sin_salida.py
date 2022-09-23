"""
1. 0
2. posicion invalida, x no se  usa
3. 70
4. Es posible contar a un mismo atleta varias veces.
"""

def listar_aeropuertos_sin_salida(vuelos: dict) -> list:
    con_destino =[]
    con_origen = []
    sin_salida = []
    for cada_vuelo in vuelos:
        if not vuelos[cada_vuelo]["destino"] in con_destino:
            con_destino.append(vuelos[cada_vuelo]["destino"])
        if not vuelos[cada_vuelo]["origen"] in con_origen:
            con_origen.append(vuelos[cada_vuelo]["origen"]) 
    for aeropuerto in con_destino:
        if aeropuerto not in con_origen:
            sin_salida.append(aeropuerto)
    
    return sin_salida