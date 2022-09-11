#import math
#def vel_en_caida_libre(altura: float) -> float:
#    g = 9.8
#    return round(math.sqrt(2*g*altura), 2)
#
#print(vel_en_caida_libre(98))

from datetime import datetime, timedelta




#def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio: int, dia_actual: int, mes_actual: int, anio_actual: int)->str:
#    fecha_nacimiento = datetime.strptime(f"{dia_nacio}/{mes_nacio}/{anio_nacio}", "%d/%m/%Y")
#    edad = relativedelta(datetime(anio_actual, mes_actual, dia_actual), fecha_nacimiento)
#    return f"{edad.years},{edad.months},{edad.days}"
#
#print(calcular_edad(20, 11, 1986, 16, 10, 1987))

#def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio: int, dia_actual: int, mes_actual: int, anio_actual: int)->str:
#    fecha_nacimiento = datetime.strptime(f"{dia_nacio}/{mes_nacio}/{anio_nacio}", "%d/%m/%Y")
#    fecha_actual = datetime.strptime(f"{dia_actual}/{mes_actual}/{anio_actual}", "%d/%m/%Y")
#    diferencia = fecha_actual-fecha_nacimiento
#
#    anios = diferencia.days//360
#    meses = (diferencia.days - (anios*360))//30.417
#    dias = diferencia.days - (anios*360) - (meses*30)
#    return f"{anios}, {meses:.0f}, {dias:.0f}"
#
#print(calcular_edad(20, 11, 1986, 16, 10, 1987))

def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio: int, dia_actual: int, mes_actual: int, anio_actual: int)->str:
    diasTotalesActuales = dia_actual +  (anio_actual*360) + (mes_actual*30)
    diasTotales =  dia_nacio + (anio_nacio*360) + (mes_nacio*30)
    diasEdad = diasTotalesActuales - diasTotales
    anios = 0
    meses = 0
    dias = 0
    while diasEdad >= 360:
        anios += 1
        diasEdad -= 360
    while diasEdad >= 30:
        meses += 1
        diasEdad -= 30

    dias = diasEdad
    return f"{anios},{meses},{dias}"


print(calcular_edad(25, 10, 1993, 4, 8, 2019))


