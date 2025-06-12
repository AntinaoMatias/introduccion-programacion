#Datos de tipo compuesto o complejo
#Son colecciones de datos de tipo simple o compuesto

#LISTAS
#Una lista es una colección ordenada de elementos de cualquier tipo de datos.
#Los elementos se separan por comas
#Además de ser una colección ordenada, es mutable, puede modificarse
lista_1 = ["cadenas de texto", 10, True, 4.55, [1, 2, 3, 4, 5]]
print(type(lista_1))
#El método len (abreviación de lenght) devuelve la cantidad de elementos
print(len(lista_1))
#print(lista_1)
#El primer elemento tendrá la posición cero.
#Para llamar el primer elemento usaremos:
print(lista_1[0])
#Nos devolverá el elemento "cadenas de texto"

#Para MODIFICAR modificar un elemento de una lista usaremos:
lista_1[0] = "Aquiles Caigo"
print(lista_1)
#Para AGREGAR un elemento a la lista usaremos .append de la siguiente manera
#Con este código agregaremos elementos al final de la lista. En este caso un 1
lista_1.append(1)

#Para ELIMINAR EL ÚLTIMO elemento de una lista usaremos .pop
lista_1.pop
print(lista_1)
#Para ELIMINAR un elemento ESPECÍFICO de la lista usaremos .pop[posición]
lista_1.pop(4)
print(lista_1)
#Para ELIMINAR TODOS los elementos de una lista usaremos .clear
lista_1.clear
print(lista_1)
#Para INSERTAR un elemento usaremos .insert y la posición donde lo quieres poner
#Pues se insertará antes de esa posición
#Usaremos lista.insert(posicion, elemento)
lista_1.insert(2, "test")