def promedio_fila(matriz :list,fila :str)->float:
    cant_estudiantes = 0
    suma = 0
    promedio = 0
    if fila > len(matriz) or fila <= 0:
        promedio = -1
    else:    
       for j in range(0,len(matriz[0])):
         suma +=matriz[fila-1][j]
         if matriz[fila-1][j] != 0:
             cant_estudiantes +=1
       if cant_estudiantes > 0:       
          promedio = round(suma/cant_estudiantes,2)
          
    return promedio