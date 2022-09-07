import calculadora_indices as calc

def ejecutar_calcular_calorias_en_actividad()->None:
    peso = float(input("Ingrese su peso (en kilogramos): "))
    altura = float(input("Ingrese su altura (en centimetros): "))
    edad = float(input("Ingrese su edad: "))
    valor_genero = float(input("Ingrese el valor del genero: "))
    valor_actividad = float(input("Ingrese el valor de la actividad: "))
    print(f"{calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)} cal")

ejecutar_calcular_calorias_en_actividad()