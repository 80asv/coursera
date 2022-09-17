def picas_y_fijas(numero_secreto: int, intento: int)->int:
    dicc = {"PICAS":0, "FIJAS":0}
    num_referencia = numero_secreto
    while intento > 0:
        i = num_referencia % 10 # toma el ultimo digito del numero secreto
        j = intento % 10 # toma la ultima cifra del intento
        if i == j:
            dicc["FIJAS"] += 1
        elif str(j) in str(numero_secreto):
            dicc["PICAS"] += 1
        # Eliminamos la ultima cifra para seguir con el siguiente digito
        num_referencia = num_referencia // 10
        intento = intento // 10

    return dicc