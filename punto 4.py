def determinar_signo(x):
    if x > 0:
        return "Positivo"
    elif x < 0:
        return "Negativo"
    else:
        return "Cero"

x = float(input("Ingrese un número real: "))
signo = determinar_signo(x)

if signo == "Positivo":
    print(f"El número {x} es positivo.")
elif signo == "Negativo":
    print(f"El número {x} es negativo.")
else:
    print(f"El número {x} es el neutro para la suma.")