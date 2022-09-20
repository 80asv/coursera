def caracteres_repetidos(cadena: str)->int:
    letras = {}
    cont = 0
    for letra in cadena:
        if letra in letras:
            if letras[letra] == 1:
                contador += 1
            letras[letra] += 1
        else:
            letras[letra] = 1
    
    return cont