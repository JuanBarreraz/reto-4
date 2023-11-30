import math

def es_punto_interior(x, y, a, b, r):
    return math.sqrt((x - a)**2 + (y - b)**2) < r

x = float(input("Ingrese la coordenada x del punto: "))
y = float(input("Ingrese la coordenada y del punto: "))
a = float(input("Ingrese la coordenada x del centro del círculo: "))
b = float(input("Ingrese la coordenada y del centro del círculo: "))
r = float(input("Ingrese el radio del círculo: "))

if es_punto_interior(x, y, a, b, r):
    print(f"El punto ({x}, {y}) está dentro del círculo centrado en ({a}, {b}) con radio {r}.")
else:
    print(f"El punto ({x}, {y}) no está dentro del círculo centrado en ({a}, {b}) con radio {r}.")