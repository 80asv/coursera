def promedio_fila(matriz: int, fila: int)->float:
    suma = 0
    estudiantes = 0 
    prom = 0
    if fila <= 0 or fila > len(matriz):
        prom = -1
    else:
        for j in range (0, len(matriz[0])):
            suma += matriz[fila-1][j]
            if matriz[fila-1][j] != 0:
                estudiantes+=1
        if estudiantes > 0:
            prom = round((suma/estudiantes), 2)

    return prom
    
matriz = [
	[2.79, 3.02, 34, 5.67, 30, 22, 1, 0],
	[3.18, 2.74, 34, 5.67, 30, 22, 1, 0],
	[2.79, 3.02, 34, 5.67, 30, 22, 1, 0],
	[2.79, 0, 34, 5.67, 30, 22, 1, 0],
	[2.79, 3.02, 34, 5.67, 30, 22, 1, 0],
]

r = promedio_fila(matriz, 5)
print(r)
