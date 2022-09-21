def buscar_elemento(entrada: list, buscado: int)->bool:
    try:
        return entrada.index(buscado)
    except:
        return -1
    
r = buscar_elemento([2, 5, 0, 6, 1, 9, 9, 9], 6)

print(r)