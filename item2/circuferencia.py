import math


PI = round(math.pi, 6)

def calcular_circunferencia(radio):

    return 2 * PI * radio

radio = float(input("Por favor ingrese el radio del círculo: "))
circunferencia = calcular_circunferencia(radio)

print(f"La circunferencia del círculo con radio {radio} es {circunferencia}")
