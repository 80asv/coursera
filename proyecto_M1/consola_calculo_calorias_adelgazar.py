import calculadora_indices as calc

def ejecutar_consumo_calorias_recomendado_para_adelgazar()->None:
    peso = float(input("Ingrese su peso (en kilogramos): "))
    altura = float(input("Ingrese su altura (en centimetros): "))
    edad = float(input("Ingrese su edad: "))
    valor_genero = float(input("Ingrese el valor del genero: "))
    print(calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero))

ejecutar_consumo_calorias_recomendado_para_adelgazar()