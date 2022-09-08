#import math
#def vel_en_caida_libre(altura: float) -> float:
#    g = 9.8
#    return round(math.sqrt(2*g*altura), 2)
#
#print(vel_en_caida_libre(98))



from calendar import month
from datetime import datetime, timedelta




#def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio: int, dia_actual: int, mes_actual: int, anio_actual: int)->str:
#    fecha_nacimiento = datetime.strptime(f"{dia_nacio}/{mes_nacio}/{anio_nacio}", "%d/%m/%Y")
#    edad = relativedelta(datetime(anio_actual, mes_actual, dia_actual), fecha_nacimiento)
#    return f"{edad.years},{edad.months},{edad.days}"
#
#print(calcular_edad(20, 11, 1986, 16, 10, 1987))
def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio: int, dia_actual: int, mes_actual: int, anio_actual: int)->str:
    fecha_nacimiento = datetime.strptime(f"{dia_nacio}/{mes_nacio}/{anio_nacio}", "%d/%m/%Y")
    fecha_actual = datetime.strptime(f"{dia_actual}/{mes_actual}/{anio_actual}", "%d/%m/%Y")
    diferencia = fecha_actual-fecha_nacimiento
    diferencia = fecha_actual-fecha_nacimiento
    anios = diferencia.days//365
    meses = (diferencia.days - (anios*365)) //30.417
    dias = diferencia.days - (anios*365) - (meses*30)
    return f"{anios}, {meses:.0f}, {dias:.0f}"

print(calcular_edad(20, 11, 1986, 16, 10, 1987))