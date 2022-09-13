# Materias de agrado
# programación, matemática, filosofía y literatura

def removeAccentMark(cadena: str) -> str:
    reemplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in reemplazos:
        cadena = cadena.replace(a, b).replace(a.upper(), b.upper())
    return cadena


def conteo_de_materias(nombre_materia_1: str, nombre_materia_2: str, nombre_materia_3: str) -> int:
    ca1 = str.lower(removeAccentMark(nombre_materia_1))
    ca2 = str.lower(removeAccentMark(nombre_materia_2))
    ca3 = str.lower(removeAccentMark(nombre_materia_3))
    
    
    

    materias_de_agrado = 0
    if "programacion" in ca1 or "matematica" in ca1 or "filosofia" in ca1 or "literatura" in ca1:
        materias_de_agrado = materias_de_agrado + 1  
    if "programacion" in ca2 or "matematica" in ca2 or "filosofia" in ca2 or "literatura" in ca2:
        materias_de_agrado = materias_de_agrado + 1  
    if "programacion" in ca3 or "matematica" in ca3 or "filosofia" in ca3 or "literatura" in ca3:
        materias_de_agrado = materias_de_agrado + 1  

    return materias_de_agrado


print(conteo_de_materias("PROGRAMACIÓN", "Inglés", "Filosofía"))