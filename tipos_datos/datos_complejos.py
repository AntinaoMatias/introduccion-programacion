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
print(lista_1)

                                   #DICCIONARIOS

#Un diccionario es una colección ORDENADA y MUTABLE de PARES de elementos de cualquier tipo de datos.
#Los elementos se separan por comas
#El primer elemento es la clave y el segundo es el valor
diccionario1 = {
    "nombre":"Esteban",
    "apellido":"Quito",
    "Profesor": True,
    "edad": 40
}
print(diccionario1)
print(type(diccionario1))
print(diccionario1["nombre"])
print(diccionario1["apellido"])
#Con .keys() podemos ver las claves y con .values()
print(diccionario1.keys())
print(diccionario1.values())
#Con .items() creará duplas dentro de una lista, como [(clave, valor), (clave, valor)]
print(diccionario1.items())

#MODIFICAR un valor
diccionario1["edad"] = 45
print(diccionario1)
#ELIMINAR el último elemento con .popitem()
diccionario1.popitem()
print(diccionario1)
#AGREGAR elementos añadiendo una clave y un valor
#Escribiremos una clave que no exista pues si ya existe, se modificará el valor
diccionario1["ciudad"] = "Temuco"
print(diccionario1)

#VACIAR un diccionario con .clear()
diccionario1.clear()
print(diccionario1)

                                    #CONJUNTOS (tipo set)

#Un conjunto es una colección DESORDENADA y MUTABLE de elementos de cualquier tipo
#Los elementos se separan por comas y no tienen ningún orden
#Por lo tanto se agregan en cualquier lado y no tienen un último item
conjunto1 = {"Erick", "avion", "ciudad", True, 45, 0, 3.59}
print(type(conjunto1))
#AÑADIR elementos, estos se añadirán en cualquier lado
conjunto1.add(False)
print(conjunto1)

#No podemos usar el pop, pues como no tenemos un último ítem, borrará cualquier elemento
#ELIMINAR elemnto especifico con  .remove(elemento)
diccionario1.remove()

#UPDATE?
#SUBCONJUTO saber si un conjunto es subconjunto de otro con" .issubset"

#TUPLA
#Una tupla es una colección ORDENADA y NO MUTABLE de elementos de cualquier tipo de datos
#los elementos se separan por comas.
tupla1 = ("Erick", 49, True)
print(tupla1)
print(type(tupla1))
print(tupla1.count(49))
print(tupla1.index(49))
#No se puede agregar ni eliminar elementos, ni borrar la tupla
