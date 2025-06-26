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

