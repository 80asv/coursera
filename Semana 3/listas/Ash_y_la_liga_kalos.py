import copy
def construir_equipo_pokemon(cantidad: int, lista_pkmn: list)->list:
    list_copy = copy.deepcopy(lista_pkmn)
    nombres = []
    ite = 0
    for i in list_copy:
        del i["nombre"]
        if sum(i.values()) >= 600:
            nombres.append(lista_pkmn[ite]["nombre"])
        ite+=1
    return nombres if len(nombres)>=cantidad else None



lista = [{'nombre': "andres", 'A': 1, 'B': 800, 'C': 3},
         {'nombre': "juan", 'A': 1, 'B': 899999999, 'C': 3},
         {'nombre': "pedro", 'A': 1, 'B': 8000000, 'C': 3},
         {'nombre': "sanabria", 'A': 10, 'B': 2, 'C': 6000}]

r = construir_equipo_pokemon(4, lista)


print(r)
