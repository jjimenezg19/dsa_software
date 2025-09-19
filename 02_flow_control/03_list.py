###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

# Creación de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] #Lista de enteros
lista2 = ["manzanas", "peras", "bananos"]
lista3 = [1, "hola", 3.14, True] #Listas de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #Matrices

print(lista1)
print(lista2)
print(lista3)
print(lista_de_listas)

# Acceso a elementos por índice:
print("\nAcceso a elementos por índice")
print(lista2[0])
print(lista2[1])
print(lista2[-1])

print(lista_de_listas[1][1])

# Slicing (rebanado)
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # del 1 hasta el 3
print(lista1[:3]) #Los tres primeros
print(lista1[3:]) #Los tres utimos
print(lista1[:]) # Lista completa

#Hay mas magia
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista1[::2]) #Para devolver indices pares
print(lista1[::-1]) #para devolver indices invertidos

#Midificar una lista
lista1[0] = 20
print(lista1)

# Añadir elementos a una lista
lista1 = [1, 2, 3]

#Forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

#Forma corta y más eficiente
lista1 += [7, 8, 9]
print(lista1)

#Recuperar longitud de una lista
longitud = len(lista1)
print(f"Longitud de la lista: {longitud} ")

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
print("Ejercicio 1: El mensaje secreto")

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
mensaje_secreto = mensaje[7:14]
##mensaje_secreto = "".join(mensaje_secreto)
mensaje_secreto = mensaje[7:14] + ["!"]
print(mensaje_secreto)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
print("\nEjercicio 2: Intercambio de posiciones")
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0]
print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
print("\nEjercicio 3: El sándwich de listas")
sandwich = pan + ingredientes + pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print("\nEjercicio 4: Duplicando la lista")
duplicados = lista[:] + lista[:]
print(duplicados)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
print("\nEjercicio 5: Duplicando la lista")
lista = [10, 20, 30, 40, 50]
centro = len(lista) // 2
print(lista[centro])


# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
print("Ejercicio 6: Reversa parcial")
lista = [1, 2, 3, 4, 5, 6]
centro = len(lista) // 2
invierte = lista[:centro][::-1] + lista[centro:]
print(invierte)