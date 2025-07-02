# Crear una función que permita convertir temperaturas Kelvin, Celsius, Farenheit
# Celsius a Farenheit
# Farenheit a Celsius
# Celsius a Kelvin
# Kelvin a Celsius
# Farenheit a Kelvin

def celsius_to_farenheit(temperatura):
    try:
        resultado = (temperatura * 9/5) + 32
        return round(resultado)
    except:
        print("Valor no corresponde")

def farenheit_to_celsius(temperatura):
    try:
        resultado = (temperatura -32) * 5/9
        return round(resultado)
    except:
        print("Valor no corresponde")

def celsius_kelvin(temperatura):
    try:
        resultado = temperatura + 273.15
        return round(resultado)
    except:
        print("Valor no corresponde")

def kelvin_to_celsius(temperatura):
    try:
        resultado = temperatura - 273.15
        return round(resultado)
    except:
        print("Valor no corresponde")

def farenheit_to_kelvin(temperatura):
    try:
        resultado = (temperatura + 459.67) * 5/9
        return round(resultado)
    except:
        print("Valor no corresponde")

def kelvin_to_farenheit(temperatura):
    try:
        resultado = (temperatura * 9/5) - 459.67
        return round(resultado)
    except:
        print("Valor no corresponde")

continuar = True
seleccion = 1
while (continuar == True):
    # Menú de selección
    print("Seleccione la conversión a realizar")
    print("1. Celsius a Kelvin")
    print("2. Celsius a Farenheit")
    print("3. Kelvin a Celsius")
    print("4. Kelvin a Farenheit")
    print("5. Farenheit a Celsius")
    print("6. Farenheit a Kelvin")
    print("7. Detener programa")
    
    #Solo recibe 1 al 7
    while 1 < seleccion < 8:
        try:
            seleccion = int(input())
        except:
            print("El valor ingresado no e válido")
    
    if (seleccion = 1):
        temperatura = input("Ingrese la temperatura en grados celsius: ")
