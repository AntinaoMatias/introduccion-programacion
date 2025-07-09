# Con import podemos importar librerías ya hechas para Python
# O importar otro documentos .py con métodos que
# ya hayamos creado en otro lado, por ejemplo:

import ejercicio7

try:
    num1 = float(input("Ingrese primer número: "))
    num2 = float(input("Ingrese segundo número"))
    op = str(input("Ingrese la operación (+, -, *, /): "))
    print(f"El resultado de {num1} {op} {num2} es {ejercicio7.calculadora_basica_v2(num1, num2, op)}")
except:
    print("Valor ingresado no corresponde")
