def calcular_costo_boletas(cantidad_boletas: int, 
                           tipo_sala: str, 
                           hora_pico: bool, 
                           pago_tajerta_cinema: bool, 
                           reserva: bool)->int:
    salas = {
        "Dinamix": 18800,
        "3D": 15500,
        "2D": 11300
    }
    if tipo_sala == "Dinamix":
        precio_final = salas["Dinamix"]*cantidad_boletas
    elif tipo_sala == "3D":
        precio_final = salas["3D"]*cantidad_boletas
    else:
        precio_final = salas["2D"]*cantidad_boletas
    
    if not hora_pico:
        precio_final = precio_final + salas[tipo_sala]-(salas[tipo_sala]*0.1)
    if cantidad_boletas >= 3:
        precio_final = precio_final-500
    if pago_tajerta_cinema:
        precio_final = precio_final*0.05
    if reserva:
        precio_final = precio_final + (2000*cantidad_boletas)
    if hora_pico and (tipo_sala == "2D" or tipo_sala == "3D"):
        precio_final = precio_final * 1.25
    else:
        precio_final = precio_final * 1.50
    
    return round(precio_final)

res = calcular_costo_boletas(3, "Dinamix", False, True, False)

print(res)

