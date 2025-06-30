# Crear una función que permita convertir temperatura de kelvin a celsius


    def celsius(a):
        temperatura = int(round(float(a - 273.15)))
        return temperatura
    temperatura = float(input("Ingrese la temperatura en Kelvin: "))
    print(f"La temperatura en grados celsius es: {celsius(temperatura)}")