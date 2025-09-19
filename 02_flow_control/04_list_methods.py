###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

# Creamos una lista con valores
lista1 = ['a', 'b', 'c', 'd']

# Añadir o insertar elementos a la lista

# Añade un elemento al final
lista1.append('e')
print(lista1)

# Inserta un elemento en la posición que le indiquemos como primer argumento
lista1.insert(1, '@')
print(lista1)

# Agrega elementos al final de la lista
lista1.extend(['😃', '😍'])
print(lista1)


# Eliminar elementos de la lista
# Eliminar la primera aparición de la cadena de texto @
lista1.remove('@')
print(lista1)

# Eliminar el último elemento de la lista y además te lo devuelve
ultimo = lista1.pop()
print(ultimo)
print(lista1)

# Eliminar el segundo elemento de la lista (es el índice 1)
lista1.pop(1)
print(lista1)

# Eliminar por lo bestia un índice
del lista1[-1]
print(lista1)

# Eliminar todos los elementos de la lista
lista1.clear()
print(lista1)

# Eliminar un rango de elementos
lista1 = ['🐼', '🐨', '🐶', '😿', '🐹']

# eliminamos los elementos del índice 1 al 3 (no incluye el índice 3)
del lista1[1:3]
print(lista1)


# Más métodos útiles
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
print("\nEjercicio 1: Añadir y modificar elementos")
lista1 = [1,2,3,4,5]
lista1.append(6)
lista1.insert(2, 10)
lista1[0] = 0
print(lista1)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
print("\nEjercicio 2: Combinar y limpiar listas")
lista_a.extend(lista_b)
print(lista_a)
lista_a.remove(1)
elemento_eliminado = lista_a.pop(3)
print(elemento_eliminado)


# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
print("Ejercicio 3: Slicing y eliminación con del")
lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista_a[2:5]
print(lista_a)


# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
print("Ejercicio 4: Ordenar y contar")
lista_1 = [5, 2, 8, 1, 9, 4, 2]
lista_1.sort()
counting = lista_1.count(2)
print(f"El numero 2 aparece {counting} veces")
comprueba = '7' in lista_1
print(f"Es {comprueba} que el numero 7 esta en la lista")


# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
print("Ejercicio 5: Copia vs. Referencia")
original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
print(original)
print(copia_1)
print(copia_2)
print(referencia)

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
print("Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.")
lista_a =  ["Manzana", "pera", "BANANA", "naranja"]
lista_a.sort(key=str.lower)
print(lista_a)