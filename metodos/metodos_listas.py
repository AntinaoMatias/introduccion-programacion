

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# METODOS LISTAS

# Formatear string: Crea un string convirtiendo las variables en strings
# print(f"Imprimimos este string y convertimos la lista a string también, que debe ir entre corchetes: {lista1}")

#print(dir(lista1))
#append() Agrega un nuevo elemento a la colección
#   lista1.append(posición)
# copy() Copia la colección
#   lista1 = lista2.copy()
# clear() Elimina todos los elementos de la colección
#   lista2.clear()
# count() Devuelve cuantas veces se repite un elemento. Cuenta la cantidad de elementos de la colección buscando un elemento especifico
#   lista1.count(elemento_a_contar)
# len() Devuelve la cantidad de elementos de una colección
#   len(lista1)
# extend() Permite agregar elementos de otra coleccion al final de esta misma
#   lista1.extend(lista2)
# index() Entrega el índice de un determinado elemento, se busca por texto
#   lista.index(elemento)
# insert() Inserta un elemento en una posición específica, indicar el índice
#   lista.insert(indice, elemento)
# pop() Elimina el último elemento, o un elemento específico si se indica el índice
#   lista.pop(indice)
# remove() Elimina EL PRIMER elemento coincidente con un string de búsqueda, es decir, el elemento por su nombre
#   lista.remove(elemento)
# reverse() Revierte el orden de la colección
#   lista.reverse()
# sort() Si es una colección de strings, ordena alfabéticamente. Si es una colección de números, ordena de menor a mayor. Tiene que ser una lista DE UN MISMO tipo de datos
#Ambos ordenes pueden cambiarse indicando como un argumento
#   Menor a Mayor:  lista.sort()
#   Menor a mayor:  lista.sort(reverse = False)
#   Mayor a menor:  lista.sort(reverse = True)