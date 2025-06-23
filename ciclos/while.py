#WHILE evalúa una condición lógica y ejecuta sus tareas en caso de ser verdadero
#   Primero evalúa y después se ejecuta


# EJEMPLO 1
#numero = 0
#while numero <= 50:
#    numero = numero + 1
#    if numero % 2 == 0:
#        print(numero)

# EJERCICIO 1
#Solicitar un número al usuario para imprimir una tabla de
# multiplicar desde 1 hasta 10 de ese número

num_str = input("Ingrese un número para crear su tabla: ")
num_int = int(num_str)

while i < range(1, 11):
    print(f"{num_int} x {i} = {num_int * i}")
