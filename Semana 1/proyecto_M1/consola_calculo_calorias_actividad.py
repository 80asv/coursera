import calculadora_indices as calc

def ejecutar_calcular_calorias_en_actividad()->None:
    peso = float(input("Ingrese su peso (en kilogramos): "))
    altura = float(input("Ingrese su altura (en centimetros): "))
    edad = float(input("Ingrese su edad: "))
    valor_genero = float(input("Ingrese el valor 5 en caso de ser masculino y -161 en caso de ser mujer: "))
    valor_actividad = float(input("Ingrese el valor 1.55 si hace ejercicio moderado (3 a 5 días a la semana)\n " + 
                                  "y 1.725 si es deportista (6 - 7 días a la semana): "))
    print(f"{calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)} cal")

ejecutar_calcular_calorias_en_actividad()