"""
Esta funcion modifica los semestre de cada estudiante (4 diccionarios)
luego los imprime por consola
"""


def avanzar_semestre(est1: dict, est2: dict, est3: dict, est4: dict)->None:
    est1["ssc"] +=1
    est2["ssc"] +=1
    est3["ssc"] +=1
    est4["ssc"] +=1

e1 = {"nombre": "lina", "codigo": "2020101234", "genero": "femenino", "ssc": 3}
e2 = {"nombre": "Maria", "codigo": "2020101234", "genero": "femenino", "ssc": 3}
e3 = {"nombre": "Pedro", "codigo": "2020101234", "genero": "femenino", "ssc": 3}
e4 = {"nombre": "Afeo", "codigo": "2020101234", "genero": "femenino", "ssc": 3}

print("Semestre estudiante 1: ", e1["ssc"])
print("Semestre estudiante 2: ", e2["ssc"])
print("Semestre estudiante 3: ", e3["ssc"])
print("Semestre estudiante 4: ", e4["ssc"])

avanzar_semestre(e1, e2, e3, e4)

print("Nuevo semestre estudiante: 1: ", e1["ssc"])
print("Nuevo semestre estudiante: 2: ", e2["ssc"])
print("Nuevo semestre estudiante: 3: ", e3["ssc"])
print("Nuevo semestre estudiante: 4: ", e4["ssc"])
