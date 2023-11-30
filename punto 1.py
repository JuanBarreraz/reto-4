def es_vocal_minuscula(numero):
    vocales_minusculas = 'aeiou'
    return numero >= ord(vocales_minusculas[0]) and numero <= ord(vocales_minusculas[-1])

numero = 97
if es_vocal_minuscula(numero):
    print(f"{numero} es el código ASCII de una vocal minúscula.")
else:
    print(f"{numero} no es el código ASCII de una vocal minúscula.")