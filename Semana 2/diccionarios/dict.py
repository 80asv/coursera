numero = int(input("Digite un numero de tres cifras"))

conteo = {}

# sacamos el ultimo digito de un numero
digito = numero % 10

# verificar si el digito ya esta dentro del diccionario
if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1

# recortar el numero para obtener el siguiente
numero = numero // 10