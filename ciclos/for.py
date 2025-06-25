
#Recorrer una lista con FOR
#FOR es un ciclo el cual recorre todos los elementos de una
# coleccion, realizando una acción por cada uno de ellos.
# Tiene la siguiente forma:

#for elemento in lista:
#    acciones

# EJEMPLO 1:
animales = ["gato", "perro", "canario", "panda", "capibara"]

#Acá le pedimos que por cada elemento de la lista animales,
# realice una acción.
for elemento in animales:
    print(f"Mi animal es: {elemento}")

# EJEMPLO 2:
usuarios = ["Aquiles Baeza", "Wendy Sulca", "Delfin Quispe"]

for nombre in usuarios:
    print(f"Usuario: {nombre}")

#EJEMPLO 3:
contador = 0
for nombre in usuarios:
    contador = contador + 1
    print(f"Usuario {contador}: {nombre}")

#RANGE crea una coleccion de números que va de cero hasta
# x número que le indiquemos. Con forma:
# range(numero)
#También puedes usar seleccionando el primer número, 

# EJEMPLO 4:

for i in range(5):
    print(i)

for i in range(len(usuarios)):
    print(f"Usuario {i + 1}: {usuarios[i]}")

# EJEMPLO 5:

cadena = "Introducción Programación"

for letra in cadena: #Le decimos que por cada elemento, asignamos
    print(letra.upper()) #el nombre letra e imprime cada letra en mayúscula


# EJERCICIO 1
#Solicitar un número al usuario para imprimir una tabla de
# multiplicar desde 1 hasta 10 de ese número

num_str = input("Ingrese un número para crear su tabla")
num_int = int(num_str)

for i in range(1, 11):
    print(f"{num_int} * {i} = {i*num_int}")


diccionario = {
    "nombre" : "Matias",
    "apellido" : "Antinao",
    "edad" : 21
}

for clave, valor in diccionario.items:
print(f"Clave: {clave} y su valor: {valor}")

