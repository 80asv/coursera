"""
Este programa permite buscar dentro de 4 diccionarios el nombre de un estudiante
para saber si este existe o no
"""

def buscar_estudiante(est1: dict, est2: dict, est3: dict, est4: dict, nom: str)->dict:
    buscado = None

    if est1["nombre"] == nom:
        buscado = est1
    if est2["nombre"] == nom:
        buscado = est1
    if est3["nombre"] == nom:
        buscado = est1
    if est4["nombre"] == nom:
        buscado = est1

    return buscado

e1 = {"nombre": "lina", "codigo": "2020101234", "genero": "femenino"}
e2 = {"nombre": "Maria", "codigo": "2020101234", "genero": "femenino"}
e3 = {"nombre": "Pedro", "codigo": "2020101234", "genero": "femenino"}
e4 = {"nombre": "Afeo", "codigo": "2020101234", "genero": "femenino"}

nombre = "Juana"

est_buscado = buscar_estudiante(e1, e2, e3, e4, nombre)

if est_buscado is None:
    print("El estudiante no existe")
else:
    print("El estudiante existe y su codigo es: " + est_buscado["codigo"])