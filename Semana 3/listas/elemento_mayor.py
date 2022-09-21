def encontrar_mayor(entrada: list)->int:
    mayor = max(entrada, default=0)
    return mayor if len(entrada)>0 else -1

r = encontrar_mayor([2, 5, 0, 6, 1, 9, 9, 10])

print(r)