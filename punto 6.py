def es_triangulo_posible(a, b, c):
    return a < b + c and b < a + c and c < a + b

a = float(input("Ingrese la longitud del primer lado: "))
b = float(input("Ingrese la longitud del segundo lado: "))
c = float(input("Ingrese la longitud del tercer lado: "))

if es_triangulo_posible(a, b, c):
    print(f"Se puede construir un triángulo con lados de longitud {a}, {b} y {c}.")
else:
    print(f"No se puede construir un triángulo con lados de longitud {a}, {b} y {c}.")