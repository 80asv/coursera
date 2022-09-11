import conversor_moneda as lb

def ejecutar_convertir_a_dolares(trm: float) -> None:
    pesos = float(input("Ingrese la cantidad en pesos: "))
    dolares = lb.convertir_a_dolares(pesos, trm)
    print(pesos, " pesos son", round(dolares, 2), " dolares")

def ejecutar_convertir_a_pesos(trm: float) -> None:
    dolares = float(input("Ingrese la cantidad en dolares: "))
    pesos = lb.convertir_a_pesos(dolares, trm)
    print(dolares, " dolares son", round(pesos, 2), " pesos")

def iniciar_aplicacion()->None:
    trm = float(input("Ingrese la trm: "))
    ejecutar_convertir_a_dolares(trm)
    ejecutar_convertir_a_pesos(trm)

iniciar_aplicacion()