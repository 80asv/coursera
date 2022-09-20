from faulthandler import cancel_dump_traceback_later


def sucesion_fibonacci(cantidad_numeros: int)->str:
    n1 = 0
    n2 = 1
    i = 0
    cad = ""
    serie = 0
    terminar = False
    while terminar == False:
        if i >= (cantidad_numeros):
            terminar = True
        else:
            serie = (n1+n2)
            n1 = n2
            n2 = serie
            cad += f"{serie-n1},"
            i+=1

    return cad[:-1]


print(sucesion_fibonacci(9))