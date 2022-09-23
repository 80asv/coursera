def flipped_dict(dicc: dict)->dict:
    flipped = {}
    for key, value in dicc.items(): 
        if value not in flipped: 
            flipped[value] = [key] 
        else: 
            flipped[value].append(key)
    return flipped

def letra_mas_comun(cadena: str)->str:
    letras = {}
    cont = 0
    for letra in cadena:
        if letra in letras:
            if letras[letra] == 1:
                cont += 1
            letras[letra] += 1
        else:
            letras[letra] = 1
    for l in letras.copy().keys():
        if l == " " or l == "." or l == ",":
            del letras[l]

    flipped = flipped_dict(letras)
    print(flipped)
    mayor_letra = sorted(flipped[max(flipped.keys())])
    
    
    return max(flipped.keys()) if len(flipped)<1 else mayor_letra[-1]

print(letra_mas_comun("ABCDsswwEEFGZHJ..."))