"""
Esta funcion indentifica que estudiantes tiene un promedio por debajo de 3.4
"""

def quienes_en_riesgo(est1: dict, est2: dict, est3: dict, est4: dict)->dict:
    en_riesgo = {}

    if est1["promedio"] < 3.4:
        en_riesgo[est1["codigo"]] = est1["promedio"]
    if est2["promedio"] < 3.4:
        en_riesgo[est2["codigo"]] = est2["promedio"]
    if est3["promedio"] < 3.4:
        en_riesgo[est3["codigo"]] = est3["promedio"]
    if est4["promedio"] < 3.4:
        en_riesgo[est4["codigo"]] = est4["promedio"]

    return en_riesgo

e1 = {"nombre": "lina", "codigo": "2020101234", "genero": "femenino", "ssc": 3, "promedio": 3.4}
e2 = {"nombre": "Maria", "codigo": "2020234", "genero": "femenino", "ssc": 3, "promedio": 3}
e3 = {"nombre": "Pedro", "codigo": "202024", "genero": "femenino", "ssc": 3, "promedio": 1.7}
e4 = {"nombre": "Afeo", "codigo": "20201434212234", "genero": "femenino", "ssc": 3, "promedio": 2.7}

print(quienes_en_riesgo(e1, e2, e3, e4))
    
