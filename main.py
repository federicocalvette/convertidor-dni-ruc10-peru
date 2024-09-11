def calcular_ruc10(dni):
    prefijo = "10"

    numero_base = prefijo + str(dni)

    coeficientes = [2, 3, 4, 5, 6, 7]

    suma = 0
    longitud = len(numero_base)

    for i in range(longitud):
        digito = int(numero_base[longitud - 1 - i])
        coeficiente = coeficientes[i % len(coeficientes)]
        suma += digito * coeficiente

    residuo = suma % 11
    digito_verificador = 11 - residuo

    if digito_verificador == 10:
        digito_verificador = 0
    elif digito_verificador == 11:
        digito_verificador = 1

    ruc10 = numero_base + str(digito_verificador)

    return ruc10


dni = input("Ingrese su DNI: ")

if len(dni) == 8 and dni.isdigit():
    ruc10 = calcular_ruc10(dni)
    print(f"El RUC 10 correspondiente al DNI {dni} es: {ruc10}")
else:
    print("El DNI ingresado no es válido. Debe ser un número de 8 dígitos.")
