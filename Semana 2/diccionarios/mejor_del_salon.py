import operator


def sacar_promedio(dicci: dict)->int:
    promedio = (dicci["matematicas"]+dicci["español"]+dicci["ciencias"]+dicci["literatura"]+dicci["arte"])/5
    return promedio

def mejor_del_salon(estudiante1: dict, estudiante2: dict, estudiante3: dict, estudiante4: dict, estudiante5: dict)->str:
    prom_est1 = sacar_promedio(estudiante1)
    prom_est2 = sacar_promedio(estudiante2)
    prom_est3 = sacar_promedio(estudiante3)
    prom_est4 = sacar_promedio(estudiante4)
    prom_est5 = sacar_promedio(estudiante5)
    promedios = {
        estudiante1["nombre"]: prom_est1,
        estudiante2["nombre"]: prom_est2,
        estudiante3["nombre"]: prom_est3,
        estudiante4["nombre"]: prom_est4,
        estudiante5["nombre"]: prom_est5
    }
    
    promedio_max = max(promedios.items(), key=operator.itemgetter(1))[0]


    return promedio_max
        

    
estudiante1 = {'nombre': 'pablo', 'matematicas': 3.4, 'español': 5.0, 'ciencias': 2.9, 'literatura': 4.2, 'arte': 3.2}
estudiante2 = {'nombre': 'andres', 'matematicas': 2.1, 'español': 5.0, 'ciencias': 3.0, 'literatura': 4.1, 'arte': 3.5}
estudiante3 = {'nombre': 'daniela', 'matematicas': 5.0, 'español': 4.2, 'ciencias': 4.4, 'literatura': 3.5, 'arte': 4.7}
estudiante4 = {'nombre': 'maria', 'matematicas': 3.2, 'español': 3.7, 'ciencias': 3.1, 'literatura': 4.7, 'arte': 3.4}
estudiante5 = {'nombre': 'Pedro', 'matematicas': 5.0, 'español': 4.2, 'ciencias': 4.4, 'literatura': 3.5, 'arte': 4.7}


print(mejor_del_salon(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5))