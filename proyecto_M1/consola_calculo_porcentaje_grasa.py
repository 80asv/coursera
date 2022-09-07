import calculadora_indices as calc

def ejecutar_calcular_porcentaje_grasa()->None:
    peso = float(input("Ingrese su peso (en kilogramos): "))
    altura = float(input("Ingrese su altura (en metros): "))
    edad = float(input("Ingrese su edad: "))
    valor_genero = float(input("Ingrese el valor del genero: "))
    print(f"{calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)}%")

ejecutar_calcular_porcentaje_grasa()