def calcular_definitivas(estudiantes: list)->list:
    estudiantes_copy = estudiantes.copy()

    for i in estudiantes_copy:
        if i["nota"] >= 4.5:
            i["nota"] = 5.0
        elif i["nota"] >= 3.5 and i["nota"] < 4.5:
            i["nota"] = 4.0
        elif i["nota"] >= 2.5 and i["nota"] < 3.5:
            i["nota"] = 3.0
        else:
            i["nota"] = 1.5
    
    return estudiantes_copy

        