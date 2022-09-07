def calcular_IMC(peso: float, altura: float) -> float:
    return round(peso/(altura**2), 2)

def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    imc = peso/(altura**2)
    return round((1.2 * imc) + (0.23 * edad) - 5.4 - valor_genero, 2)

def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int) -> float:
    return round((10*peso) + (6.25*altura) - (5*edad) + valor_genero, 2)

def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: int, valor_actividad: float) -> float:
    tmb = (10*peso) + (6.25*altura) - (5*edad) + valor_genero
    return round(tmb * valor_actividad, 2)

def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: int) -> str:
    valor_maximo = ((calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * 0.15) - calcular_calorias_en_reposo(peso, altura, edad, valor_genero)) * -1
    valor_minimo = ((calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * 0.20) - calcular_calorias_en_reposo(peso, altura, edad, valor_genero)) * -1
    return f"Para adelgazar es recomendado que consumas entre: {round(valor_minimo, 2)} y {round(valor_maximo, 2)} calorías al día."

