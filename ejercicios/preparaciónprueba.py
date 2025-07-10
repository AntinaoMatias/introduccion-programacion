# 1. Escriba un programa que pida 3 números y los ordene de mayor a menor

def ordenar_numeros():
    num_ordenados = []
    try:
        for i in range(3):
            numero = float(input(f"Ingrese un número: "))
            num_ordenados.append(numero)
        num_ordenados.sort(reverse = True)
        print(num_ordenados)
    except:
        print("El valor ingresado No corresponde a un número")



# 2. Escriba un programa que calcule el área y el perímetro de un cuadrado
# si cualquier valor es negativo se debe entregar un mensaje de error

def area_cuadrado():
    try:
        lado = float(input("Ingrese la medida de cualquier lado del cuadrado: "))
        if lado >= 0:
            area = lado * lado
            perimetro = lado * 4
            print(f"El área de tu cuadrado es: {area} y el perímetro: {perimetro}")
        else:
            print("No se permiten valores negativos")
    except:
        print("El valor ingresado no corresponde a un número")



# 3 Escriba un programa que pida el precio de un producto y calcule el valor del IVA
# si el precio es negativo se debe entregar un mensaje de error

def calcular_iva():
    try:
        precio = float(input("Ingrese el precio del producto sin IVA: "))
        if (precio >= 0):
            print(f"El precio con Iva es igual a ${round(precio * 1.19)}")
        else:
            print("El precio no puede ser un número negativo")
    except:
        print("El valor ingresado no corresponde a un número")

# 4 Escriba un programa que permita calcular el área de un triángulo, 
# si cualquier valor es negativo, se debe entregar un mensaje de error.
# Area de un triángulo: (base * altura) / 2

def area_triangulo():
    try:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        area = (base*altura) / 2
        if base >= 0 and altura >= 0:
            print(f"El area de su triángulo es: {area}")
        else:
            print("No es posible calcular con números negativos.")
    except:
        print("El valor ingresado no corresponde a un número")    

# 5 Escriba una calculadora básica que pida al usuario 2 números
# y realice las 4 operaciones aritméticas básicas.
# Si se trata de dividir por 0 se deberá entregar un mensaje de error.

def menu_operaciones():
    print("1. ( + ) Sumar.")
    print("2. ( - ) Restar.")
    print("3. ( * ) Multiplicar.")
    print("4. ( / ) Dividir.")

def calculadora_basica():
    try:
        while True:
            num = float(input("Ingrese el primer número: "))
            menu_operaciones()
            operacion = float(input("Ingrese la operación a realizar: "))
            num2 = float(input("Ingrese el segundo número: "))
            if operacion == 1:
                print(f"{num} + {num2} es igual a {num + num2}")
            elif operacion == 2:
                print(f"{num} - {num2} es igual a {num - num2}")
            elif operacion == 3:
                print(f"{num} * {num2} es igual a {num * num2}")
            elif operacion == 4:
                print(f"{num} / {num2} es igual a {num / num2}")
            else:
                print("La opción seleccionada NO es válida")
            print("¿Desea realizar otra operación?")
            print("1. Sí")
            print("2. No")
            continuar = float(input())
            if continuar == 1:
                continue
            elif continuar == 2:
                break
            else:
                print("La opción seleccionada NO es válida")
                break
            
    except ZeroDivisionError:
        print("No es posible dividir por cero")
    except:
        print("Uno o más de los valores ingresados no corresponde")




#break rompe TODOS los ciclos
#continue vuelve al inicio del ciclo