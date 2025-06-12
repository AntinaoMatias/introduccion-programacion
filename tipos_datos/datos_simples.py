#Datos de tipo cadena de texto, o string:
'Cadena de texto'
"Otra cadena de texto"
"""Con esta tercer linea de caracteres
definimos un string con uno o más
saltos de linea, simplemente comenzando
y terminando con triple comillas
Funciona con simples y dobles"""

#Comando print para imprimir información
print("Esto es una cadena de texto")
print('Esto es una cadena de texto')
print('Esto es una cadena de texto con "comillas dobles"')
print("Esto es una cadena de texto con 'comillas simples'")

#Crear una variable para almacenar strings
cadena_texto_1 = "Hola, Don Pepito"
cadena_texto_2 = "Hola, Don José"
cadena_texto_3 = "¿Pasó usted ya por casa?"
cadena_texto_4 = "Por su casa yo pasé"
cadena_texto_5 = "¿Vio usted a mi abuela?"
cadena_texto_6 = "A su abuela yo la ví"
despedida1 = "Adiós Don Pepito"
despedida2 = "Adiós Don José"

print(cadena_texto_1)
print(cadena_texto_2)
print(cadena_texto_3)
print(cadena_texto_4)
print(cadena_texto_5)
print(cadena_texto_6)
print(despedida1)
print(despedida2)

#Ejemplo 2: Usaremos input() para recibir datos del usuario

saludo = "Buenos días"
nombre = input("Escriba su nombre: ")
#Creamos una variable para concatenar dos cadenas
texto_final = saludo + " " + nombre
print(texto_final)

#De esta manera escribimos comentarios
#Estos no se ejecutarán con el código

#Datos de tipo numéricos
#Tipo int
numero_entero = 49
#Tipo float
numero_decimal = 49.99

#Datos de tipo lógico (booleanos)
#Tipo bool
dato_verdadero = True
dato_falso = False

num1 = 35
num2 = 12.65
print(num1*num2)

#Con el método type nos devuelve el tipo de dato de una variable
print(type(numero_entero))