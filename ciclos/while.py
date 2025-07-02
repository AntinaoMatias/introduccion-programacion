#WHILE evalúa una condición lógica y ejecuta sus tareas en caso de ser verdadero
#   Primero evalúa y después se ejecuta


# EJEMPLO 1
numero = 0
while numero <= 50:
    numero = numero + 1
    if numero % 2 == 0:
        print(numero)

# EJERCICIO 1
#Solicitar un número al usuario para imprimir una tabla de
# multiplicar desde 1 hasta 10 de ese número

#num_str = input("Ingrese un número para crear su tabla: ")
#num_int = int(num_str)
#i = 1
#print("Su tabla es: ")
#while i < 11:
#    print(f"{num_int} x {i} = {num_int * i}")
#    i += 1

#Escriba un programa que escriba las tablas de multiplicar del 1 al 10




print("Seleccione el método a usar")

usar = "for"
#usar = "while"

print("Tablas de multiplicar: ")

if (usar == "while"):
    i = 1
    e = 1
    while i < 11:
        print("============")
        print(f"Tabla del {i}")
        print("============")
        while e < 11:
            print(f"{i} x {e} = {i * e}")
            e += 1
        e = 1
        i += 1

if (usar == "for"):
    for i in range(1, 11):
        print("============")
        print(f"Tabla del {i}")
        print("============")
        for e in range(1, 11):
            print(f"{i} x {e} = {i * e}")
            e += 1
    e = 1
    i += 1

#En el FOR no es necesario definir las variables,
# pues se definen dentro del rango después de in