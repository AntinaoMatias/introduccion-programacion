#Un MÉTODO es una función de programación que ejecuta una tarea específica

#El método DIR nos indica todos los métodos disponibles con el tipo de datos
print("Usaremos dir para ver los métodos para strings")
print(dir(str))
#Devuelve: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
#Probaremos .capitilize que nos servirá para capitalizar un string
#es decir, convertirá la primera palabra en mayúscula 

nombre = "matias antinao"
asignatura = "INTRODUCCIÓN A LA COMPUTACIÓN"

print(nombre.capitalize())

#Ahora .title convertirá la primera letra de cada palabra en mayúscula
print(nombre.title())

#Ahora .upper convertirá todo el string en mayúsculas
print(nombre.upper())

#Y .lower convertirá todo en minúsculas
print(asignatura.lower())

#Otro médoto como .count cuenta en el string, ejemplo, este contará todas las a de la variable nombre
print(nombre.count("a"))

#Y .find devuelve el índice (posición de un elemento dentro de una colección)
#en la que encuentras
#Cuando no lo encuentra da -1
print(nombre.find("o"))

# .endswith nos devolverá si un string termina en cierto elemento
print(nombre.endswith("o"))