#- 1 Cree una lista de números enteros y ordénela en orden ascendente utilizando el método de lista integrado.

# números_enteros = [0, 1, 3, 5, 2, 9, 12, 4, 8]

# números_enteros.sort()
# print(números_enteros)

#- 2 Dada una lista de cadenas, cree un nuevo conjunto que contenga solo las cadenas únicas en la lista.

# lista_de_cadenas = [0, 2, 3, 0, 2, 4, 6, 4, 5, 6]

# repetidos = []

# descartados = []

# for n in lista_de_cadenas:
#     if n not in descartados:
#         descartados.append(n)
#     else:
#         repetidos.append(n)

# print(repetidos)

#- 3 Cree una tupla que contenga varios elementos,
# luego use una sentencia de impresión formateada para imprimir cada elemento de la tupla en una línea separada.


# mi_tupla = (23, "Hola", 4.5, True)


# for elemento in mi_tupla:
#     print("{}\n".format(elemento))


#- 4  Dada una lista de números enteros,
# utilice una comprensión de lista para crear una nueva lista que contenga solo los números pares de la lista original.

# numeros = [1, 2, 3, 4, 5, 6]

# numeros_pares = [numero for numero in numeros if numero % 2 == 0]

# print(numeros_pares)

#- 5 Cree una lista de diccionarios, donde cada diccionario represente una persona con las claves "nombre", "edad" y "profesión".
# Luego, use una comprensión de lista para crear una lista de todas las profesiones de las personas en la lista original.

# Personas = [
#     {"nombre": "Jordi", "edad": 27, "profesión": "cocinero"},
#     {"nombre": "Tomás", "edad": 24, "profesión": "Teleoperador"},
#     {"nombre": "Giorgio", "edad": 27, "profesión": "Pizzero"},
#     {"nombre": "Mario", "edad": 23, "profesión": "estudiante"},
# ]

# profesiones = [persona["profesión"] for persona in Personas]

# print(profesiones)

#- 6 Dada una lista de cadenas, utilice una comprensión de lista para crear una nueva lista que contenga solo las cadenas que tienen más de 5 caracteres.


# lista = ["Hola", "Python", "es", "genial", "para", "aprender"]


# lista_mas_larga = [cadena for cadena in lista if len(cadena) > 5]


# print(lista_mas_larga)

#- 7 Cree una tupla que contenga varios números enteros,
# luego utilice una sentencia de impresión formateada (f'string') para imprimir la suma y el promedio de los números en la tupla.

# numeros = (10, 20, 30, 40, 50)

# suma = sum(numeros)

# promedio = suma / len(numeros)


# print(f"La suma es {suma}")
# print(f"El promedio es {promedio}")

#- 8 Dada una lista de números enteros,
# cree una nueva lista que contenga los números únicos en la lista original,
# pero en orden inverso.

# numeros =[1, 2, 3, 4, 5, 6, 7, 8]

# numeros_invertidos = list(reversed(list(set(numeros))))

# print(numeros_invertidos)

#- 9 Dada una lista de cadenas, utilice una comprensión de lista para crear una nueva lista que contenga solo las cadenas que comienzan con la letra "a".

# lista = ["agua", "ropa", "arena", "ordenador", "aleta"]

# lista_que_inicia_con_a = [lista for lista in lista if lista.startswith("a")]

# print(lista_que_inicia_con_a)

#- 10 Cree una lista de diccionarios, donde cada diccionario represente un libro con las claves "título", "autor" y "año de publicación".
# Luego crear una lista de todos los autores de libros publicados antes de 2000.

libros = [
    {"titulo": "El archivo de las tormentas", "autor": "Brandon Sanderson", "año de publicación" : 2014},
    {"titulo": "El último deseo", "autor": "Andrzej Sapkowski", "año de publicación" : 1993},
    {"titulo": "Harry Potter y la piedra filosofal", "autor": "J. K. Rowling", "año de publicación" : 1997}
]

autores_antes_2000 = [libro["autor"] for libro in libros if libro["año de publicación"] < 2000]

print(autores_antes_2000)