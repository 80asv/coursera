import calculadora_indices as calc

def ejecutar_calcular_calorias_en_reposo()->None:
    peso = float(input("Ingrese su peso (en kilogramos): "))
    altura = float(input("Ingrese su altura (en centimetros): "))
    edad = float(input("Ingrese su edad: "))
    valor_genero = float(input("Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: "))
    print(f"{calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)} cal")

ejecutar_calcular_calorias_en_reposo()