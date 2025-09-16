import math

def sigmoid(x):
    """Calcula el valor de la función sigmoide para cualquier x."""
    return 1 / (1 + math.exp(-x))

def interpretar_sigmoid(x, resultado):
    """Devuelve una interpretación según el valor de x y su salida sigmoide."""
    if x < -5:
        return "Muy negativo: la salida se aproxima a 0 (neurona no activada)"
    elif x < 0:
        return "Negativo: la salida es baja, pero no nula"
    elif x == 0:
        return "Neutro: la salida es 0.5, punto medio de activación"
    elif x < 5:
        return "Positivo: la salida es alta, la neurona se activa"
    else:
        return "Muy positivo: la salida se aproxima a 1 (neurona activada completamente)"

# Entrada dinámica
try:
    x = float(input("Ingresá un valor para x: "))
    resultado = sigmoid(x)
    interpretacion = interpretar_sigmoid(x, resultado)

    print(f"\nResultado:")
    print(f"sigmoid({x}) = {resultado:.5f}")
    print(f"Interpretación: {interpretacion}")

except ValueError:
    print("Por favor, ingresá un número válido.")
