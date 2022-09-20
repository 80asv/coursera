import operator

def mejor_de_cada_curso(estudiante1: dict, estudiante2: dict, estudiante3: dict, estudiante4: dict, estudiante5: dict)->dict:
    mejor_mate = {
        estudiante1["nombre"]: estudiante1["matematicas"],
        estudiante2["nombre"]: estudiante2["matematicas"],
        estudiante3["nombre"]: estudiante3["matematicas"],
        estudiante4["nombre"]: estudiante4["matematicas"],
        estudiante5["nombre"]: estudiante5["matematicas"]
    }
    mejor_spnl = {
        estudiante1["nombre"]: estudiante1["español"],
        estudiante2["nombre"]: estudiante2["español"],
        estudiante3["nombre"]: estudiante3["español"],
        estudiante4["nombre"]: estudiante4["español"],
        estudiante5["nombre"]: estudiante5["español"]
    }
    mejor_sci = {
        estudiante1["nombre"]: estudiante1["ciencias"],
        estudiante2["nombre"]: estudiante2["ciencias"],
        estudiante3["nombre"]: estudiante3["ciencias"],
        estudiante4["nombre"]: estudiante4["ciencias"],
        estudiante5["nombre"]: estudiante5["ciencias"]
    }
    mejor_lit = {
        estudiante1["nombre"]: estudiante1["literatura"],
        estudiante2["nombre"]: estudiante2["literatura"],
        estudiante3["nombre"]: estudiante3["literatura"],
        estudiante4["nombre"]: estudiante4["literatura"],
        estudiante5["nombre"]: estudiante5["literatura"]
    }
    mejor_art = {
        estudiante1["nombre"]: estudiante1["arte"],
        estudiante2["nombre"]: estudiante2["arte"],
        estudiante3["nombre"]: estudiante3["arte"],
        estudiante4["nombre"]: estudiante4["arte"],
        estudiante5["nombre"]: estudiante5["arte"]
    }





    mejores = {
        "matematicas": max(mejor_mate.items(), key=operator.itemgetter(1))[0],
        "español": max(mejor_spnl.items(), key=operator.itemgetter(0))[0],
        "ciencias": max(mejor_sci.items(), key=operator.itemgetter(0))[0],
        "literatura": max(mejor_lit.items(), key=operator.itemgetter(0))[0],
        "arte": max(mejor_art.items(), key=operator.itemgetter(0))[0],
    }

    
    
    return mejores


    
estudiante1 = {'nombre': 'pablo', 'matematicas': 3.4, 'español': 5.0, 'ciencias': 2.9, 'literatura': 4.2, 'arte': 3.2}
estudiante2 = {'nombre': 'andres', 'matematicas': 2.1, 'español': 5.0, 'ciencias': 3.0, 'literatura': 4.1, 'arte': 3.5}
estudiante3 = {'nombre': 'daniela', 'matematicas': 5.0, 'español': 4.2, 'ciencias': 4.4, 'literatura': 3.5, 'arte': 4.7}
estudiante4 = {'nombre': 'maria', 'matematicas': 3.2, 'español': 3.7, 'ciencias': 3.1, 'literatura': 4.7, 'arte': 3.4}
estudiante5 = {'nombre': 'Pedro', 'matematicas': 5.0, 'español': 4.2, 'ciencias': 4.4, 'literatura': 3.5, 'arte': 4.7}


print(mejor_de_cada_curso(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5))
