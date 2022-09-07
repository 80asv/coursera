def  calcular_BMI(peso_lb: float, altura_inch: float) -> float:
    result = (peso_lb*0.45)/(altura_inch*0.025)**2
    return round(result, 2)

print(calcular_BMI(220, 78))
