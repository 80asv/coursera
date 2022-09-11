import calculadora_indices as calc

def ejecutar_calcular_IMC()->None:
    peso = float(input("Ingrese su peso (en kilogramos): "))
    altura = float(input("Ingrese su altura (en metros): "))
    print(calc.calcular_IMC(peso, altura))

ejecutar_calcular_IMC()