#-*- coding: utf  -8 -*-
 
def calcular_horario_llegada(hora_salida: int,minuto_salida: int,segundo_salida: int,duracion_horas: int,duracion_minutos: int,duracion_segundos: int) -> str:
    minutos,segundos = divmod(segundo_salida+duracion_segundos,60)
    horas,minutos = divmod(minutos+minuto_salida+duracion_minutos,60)
    horas +=  hora_salida + duracion_horas
    if horas > 24:horas -= 24
    return f"{horas}:{minutos}:{segundos}"

print(calcular_horario_llegada(23, 30, 0, 0, 40, 20))