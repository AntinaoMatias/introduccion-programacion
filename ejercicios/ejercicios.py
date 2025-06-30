#Pida al usuario 2 numeros
#Muestre su suma, su resta, su multiplicación y su division
#Si el divisor es cero, muestra error


num = int(round(float(input("Ingrese el primer número: "))))
num2 = int(round(float(input("Ingrese el segundo número: "))))

print(f"{num} + {num2} = {num+num2}")
print(f"{num} - {num2} = {num-num2}")
print(f"{num} * {num2} = {num*num2}")
if num2 is not 0:
    print(f"{num} / {num2} = {num/num2}")
else:
    print("No está definido dividir por cero")



numeros = []
for i in range(5):
    num = float(input("Ingrese un número: "))
    numeros.append(num)
print(f"La suma de los números {numeros} es igual a {sum(numeros)}")


# Como hacer que un input no pueda estar vacío en Python
#Para ello usamos TRY: que es un intento y en EXCEPT: que indicará el error
# De la siguiente forma:

numeros = []
for i in range(5):
    try:
        num = float(input("Ingrese un número: "))
        numeros.append(num)
    except ValueError:
        print("Valor ingresado NO corresponde")
        numeros.append(0)
    except:
        print("Error desconocido")
print(f"La suma de los números {numeros} es igual a {sum(numeros)}")

# Tratamos por errores ZeroDivisionError y ValueError
# Con except ZeroDivisionError:
# Con except ValueError:
# O un except general, para cualquier tipo de error
# except:

try:
    a = int(input("Ingrese el numerador: "))
    b = int(input("Ingrese el denominador: "))
    division = a/b
    print(f"El resultado de {a}/{b} es igual a {division}")
except ZeroDivisionError:
    print("No está definido dividir por cero")
except ValueError:
    print("Valor ingresado NO corresponde")
except:
    print("Error inesperado")
