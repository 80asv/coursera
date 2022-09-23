def calcular_estadisticas_tarea(estudiantes_tareas: dict, nombre_tarea: str)->dict:
    dicc = {}
    notas_tarea = {}
    i = 0
    cantidad = 0
    for alumno, tareas in estudiantes_tareas.items():
        if nombre_tarea in tareas:
            notas_tarea[alumno] = tareas[nombre_tarea]
            cantidad+=1

    
        
    dicc["mayor"] = max(notas_tarea.values())
    dicc["mejor"] = max(notas_tarea, key=lambda key: notas_tarea[key])
    dicc["menor"] = min(notas_tarea.values())
    dicc["peor"] = min(notas_tarea, key=lambda key: notas_tarea[key])
    dicc["promedio"] = sum(notas_tarea.values())/len(notas_tarea)
    dicc["cantidad"] = cantidad
    dicc["total"] = sum(notas_tarea.values())

    return dicc
        




d1 =  {"Roberto": {"Tarea 1": 0, "Tarea 2" : 910, "Tarea 3" : 910},
       "pedro": {"Tarea 2" : 0,"Tarea 3" : 910},
       "luis": {"Tarea 1": 867, "Tarea 2" : 3, },}


r = calcular_estadisticas_tarea(d1, "Tarea 1")

print(r)
#print(r)