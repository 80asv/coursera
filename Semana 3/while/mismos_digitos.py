def mismoLen(lista1: list, lista2: list)->bool:
    terminado = False
    i = 0
    while terminado == False:
        if len(f"{lista1[i]}") == len(f"{lista2[i]}") and f"{lista1[i]}" in f"{lista2}":
            res = True
            i+=1
            if i >= len(lista1):
                terminado = True
        else:
            res = False
            terminado = True
    
    return res

def dif_len(list_menor: list, num_mayor: int)->bool:
    terminado = False
    i = 0

    while terminado == False:
        if f"{list_menor[i]}" in f"{num_mayor}":
            res = True
            i+=1
            if i>=len(list_menor):
                terminado = True
        else:
            res = False
            terminado = True
        
    return res


def mismos_digitos(a: int, b: int)->bool:
    num_a = [int(a) for a in str(a)]
    num_b = [int(a) for a in str(b)]
    num_mayor = a if len(f"{a}")>len(f"{b}") else b
    num_menor = b if len(f"{a}")>len(f"{b}") else a
    list_menor = num_b if len(num_b)<len(num_a) else num_a
    list_mayor = num_a if len(num_b)<len(num_a) else num_b

    if len(f"{a}") == len(f"{b}"):
        
        res = mismoLen(list_mayor, list_menor)
    else:
        res = dif_len(list_menor, num_mayor)
    
    return res

print(mismos_digitos(420, 402))