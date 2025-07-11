
# METODOS DICCIONARIOS

diccionario = {1 : "nombre", 2 : "apellido"}
# .clear() Elimina todos los elementos de la colección
diccionario.clear()

# .copy() Copia la colección
diccionario1 = diccionario2.copy()

# .fromkeys() Crea un nuevo diccionario recorriendo una colección de claves x y asignandoles un valor y
# dict. Crea una colección
nuevo_diccionario = dict.fromkeys(x, y)

# .get() Retorna el valor de una clave específica
diccionario.get(clave)

# .keys() Devuelve una lista con las claves del diccionario
diccionario.keys()

# .values() Devuelve una lista con los valores del diccionario
diccionario.values()

# .pop() Elimina el elemento completo (Su clave y valor) especificando la clave
diccionario.pop(clave)

# .popitem() Elimina el último elemento, incluyendo su clave y su valor
diccionario.popitem()

# .update() Actualiza o crea un elemento indicando su clave. Si la clave existe, actualiza. Si no existe la crea.
diccionario.update(clave : valor)

# items() Permite recorrer cada uno de los elementos de una colección


