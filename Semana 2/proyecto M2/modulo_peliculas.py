"""
NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

import math
import operator

def hhmm(mins: float)->str:
    """
    esta funcion recibe un valor en minutos y lo convierte en formato HH:MM
    """
    horas = mins/60
    # extraer la parte decimal de las horas, las cuales seran los minutos
    parte_decimal, parte_entera = math.modf(horas)
    # pasa la parte decimal a minutos
    parte_decimal = parte_decimal*60
    
    if parte_entera < 10:
        hh = "0" + f"{parte_entera:.0f}"
    else:
        hh = f"{parte_entera:.0f}"
        
    if parte_decimal < 10:
        mm = "0" + f"{round(parte_decimal, 2):.0f}"
    else:
        mm = f"{round(parte_decimal, 2):.0f}"
    
    # formato HH:MM
    return f"{hh}:{mm}"

def hora_pelicula(dicc: dict)->int:
    hora_inicio = (dicc["hora"]//100) * 60 + dicc["hora"] % 100
    hora_fin = hora_inicio + dicc['duracion']

    return [hora_inicio, hora_fin]


def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    pelicula = {
        "nombre": nombre,
        "genero": genero,
        "duracion": duracion,
        "anio": anio,
        "clasificacion": clasificacion,
        "hora": hora,
        "dia": dia
    }
    return pelicula
def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    buscado = None
    if p1["nombre"] == nombre_pelicula:
        buscado = p1
    if p2["nombre"] == nombre_pelicula:
        buscado = p2
    if p3["nombre"] == nombre_pelicula:
        buscado = p3
    if p4["nombre"] == nombre_pelicula:
        buscado = p4
    if p5["nombre"] == nombre_pelicula:
        buscado = p5

    return buscado
def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    
    peli_mayor = p1["duracion"]
    res = p1
 
    if p2["duracion"]>peli_mayor:
        peli_mayor=p2["duracion"]
        res=p2
    if p3["duracion"]>peli_mayor:
        peli_mayor=p3["duracion"]
        res=p3
    if p4["duracion"]>peli_mayor:
        peli_mayor=p4["duracion"]
        res=p4
    if p5["duracion"]>peli_mayor:
        peli_mayor=p5["duracion"]
        res=p5
    return res 

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
    Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
    Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    prom_pelicula_en_min = (p1["duracion"]+p2["duracion"]+p3["duracion"]+p4["duracion"]+p5["duracion"])/5
    return hhmm(prom_pelicula_en_min)

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    res_pelis = []
    resultado = ""

    if p1["anio"]>anio:
        res_pelis.append(p1["nombre"])
    if p2["anio"]>anio:
        res_pelis.append(p2["nombre"])
    if p3["anio"]>anio:
        res_pelis.append(p3["nombre"])
    if p4["anio"]>anio:
        res_pelis.append(p4["nombre"])
    if p5["anio"]>anio:
        res_pelis.append(p5["nombre"])

    # imprimir resultados
    if res_pelis.__len__() == 1:
        resultado = res_pelis[0]
    else:
        for n in res_pelis:
            resultado += f"{n}, "
        resultado = resultado[:-2]

    return resultado
def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    
    contador = 0

    if p1["clasificacion"] == "18+":
        contador = contador + 1
    if p2["clasificacion"] == "18+":
        contador = contador + 1
    if p3["clasificacion"] == "18+":
        contador = contador + 1
    if p4["clasificacion"] == "18+":
        contador = contador + 1
    if p5["clasificacion"] == "18+":
        contador = contador + 1


    return contador


def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    
    hh_inicio_nueva_peli = (nueva_hora//100) * 60 + nueva_hora % 100
    hh_fin_nueva_peli = hh_inicio_nueva_peli + peli["duracion"]

    result = True

    if (nuevo_dia == p1['dia'] and (hh_inicio_nueva_peli <= hora_pelicula(p1)[1] and hh_fin_nueva_peli >= hora_pelicula(p1)[0])):
        result = False
    if (nuevo_dia == p2['dia'] and (hh_inicio_nueva_peli <= hora_pelicula(p2)[1] and hh_fin_nueva_peli >= hora_pelicula(p2)[0])):
        result = False
    if (nuevo_dia == p3['dia'] and (hh_inicio_nueva_peli <= hora_pelicula(p3)[1] and hh_fin_nueva_peli >= hora_pelicula(p3)[0])):
        result = False
    if (nuevo_dia == p4['dia'] and (hh_inicio_nueva_peli <= hora_pelicula(p4)[1] and hh_fin_nueva_peli >= hora_pelicula(p4)[0])):
        result = False
    if (nuevo_dia == p5['dia'] and (hh_inicio_nueva_peli <= hora_pelicula(p5)[1] and hh_fin_nueva_peli >= hora_pelicula(p5)[0])):
        result = False
    
    # control horario
    if control_horario:
        if "Documental" in peli["genero"] and hh_inicio_nueva_peli > (22*60):
            result = False
        if "Drama" in peli["genero"] and nuevo_dia == "Viernes":
            result = False
        if hh_inicio_nueva_peli >= 23*60 or hh_inicio_nueva_peli <= 6*60 and (nuevo_dia != "Sábado" or nuevo_dia != "Domingo"):
            result = False
    
    return result

    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    
    esta_invitado = False
    genero_peli = peli["genero"]

    if edad_invitado >= 18:
        esta_invitado = True
    #elif genero_peli == "Terror" and edad_invitado < 15:
    #    esta_invitado = False
    elif genero_peli == "Familiar" and edad_invitado <= 10:
        esta_invitado = True
    elif edad_invitado < 18 and peli["clasificacion"] == "18+" and autorizacion_padres == True:
        esta_invitado = True

    return esta_invitado









