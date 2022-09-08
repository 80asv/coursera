import calculadora_indices as calc

def ejecutar_calcular_porcentaje_grasa()->None:
    peso = float(input("Ingrese su peso (en kilogramos): "))
    altura = float(input("Ingrese su altura (en metros): "))
    edad = float(input("Ingrese su edad: "))
    valor_genero = float(input("Ingrese el valor 10.8 en caso de ser hombre y 0 en caso de ser mujer: "))
    print(f"{calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)}%")

ejecutar_calcular_porcentaje_grasa()