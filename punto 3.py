def es_digito(caracter):
    if len(caracter) != 1:
        return "El caracter debe tener exactamente un carácter."
    else:
        return caracter.isdigit()

caracter = "1"
resultado = es_digito(caracter)

if isinstance(resultado, bool):
    if resultado:
        print(f"{caracter} es un dígito.")
    else:
        print(f"{caracter} no es un dígito.")
else:
    print(resultado)