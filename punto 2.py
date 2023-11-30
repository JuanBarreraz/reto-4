def es_par(cadena):
    if len(cadena) != 1:
        return "La cadena debe tener exactamente una letra."
    else:
        codigo_ascii = ord(cadena[0])
        return codigo_ascii % 2 == 0

cadena = "a"
resultado = es_par(cadena)

if isinstance(resultado, bool):
    if resultado:
        print(f"{cadena} es una letra con código ASCII par.")
    else:
        print(f"{cadena} es una letra con código ASCII impar.")
else:
    print(resultado)