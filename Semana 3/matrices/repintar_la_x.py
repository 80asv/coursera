def pintar_x(matriz: list, operacion: str)->list:
    if operacion == "+":
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[0])):
                if i == j:
                    matriz[i][j] += matriz[i][j]
                elif ((i + j) == (len(matriz) - 1)):
                    matriz[i][j] += matriz[i][j]
                else:
                    matriz[i][j] = matriz[i][j]
    if operacion == "-":
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[0])):
                if i == j:
                    matriz[i][j] -= matriz[i][j]
                elif ((i + j) == (len(matriz) - 1)):
                    matriz[i][j] -= matriz[i][j]
                else:
                    matriz[i][j] = matriz[i][j]
    if operacion == "*":
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[0])):
                if i == j:
                    matriz[i][j] *= matriz[i][j]
                elif ((i + j) == (len(matriz) - 1)):
                    matriz[i][j] *= matriz[i][j]
                else:
                    matriz[i][j] = matriz[i][j]
    if operacion == "/":
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[0])):
                if matriz[i][j] != 0 and i == j:
                    matriz[i][j] /= matriz[i][j]
                elif matriz[i][j] != 0 and ((i + j) == (len(matriz) - 1)):
                    matriz[i][j] /= matriz[i][j]
                else:
                    matriz[i][j] = matriz[i][j]

    return matriz


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

r = pintar_x(matriz, "/")

for fila in r:
    print(fila)