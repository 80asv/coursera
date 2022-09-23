def hacer_la_vaca(salon:list,vaca:str)->list:
    mayor_aporte = 0
    suma = 0
    for i in range (0, len(salon)):
        for j in range (0, len (salon[0])):
            suma += salon[i][j]
            if mayor_aporte < salon[i][j]:
                mayor_aporte = salon[i][j]
                row = i
                column = j
    
    if "botella" in vaca and suma>=120000 or "pastel" in vaca and suma >= 35000:
        res = ["Hay Vaca"]
    if (vaca == "botella" and suma>= 120000) or (vaca == "pastel"and suma>=35000):
        res = ["Hay Vaca", row, column]
    else:
        res = ["No Alcanza", row, column]
        
    return res

matriz = [
	[1, 20, 3],
	[4, 5, 6],
	[7, 8, 9]
]

r = hacer_la_vaca(matriz, "botella")
print(r)