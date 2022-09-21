def insertar_ordenado(lista: list, cadena: str)->list:
    i = 0 
    while i < len(lista) and cadena > lista[i]:
        i+=1
    lista.insert(i, cadena)

    return lista

lista = []
palabra = input("Ingrese una palabra, o 'terminar' para cerrar: ")

while palabra != "terminar":
    insertar_ordenado(lista, palabra)
    palabra = input("Ingrese una palabra, o 'terminar' para cerrar: ")

print(lista)



