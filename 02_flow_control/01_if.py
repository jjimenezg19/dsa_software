###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os
os.system("clear")

print("\n Sentecia simple condicional")

edad = 18
if edad >= 18:
    print("Eres mayor de edad")

edad = 15
if edad >= 18:
    print("Eres mayor de edad")

print(F"\n Sentecia condicional else if")
edad = 16
if edad >= 18:
    print(f"Eres mayor de edad")
else:
    print(f"Eres menor de edad")

print(F"\n Sentecia condicional  elif")
nota = 7
if nota >= 9:
    print(f"Sobresaliente!")
elif nota >= 7:
    print(f"Notable!")
elif nota >= 5:
    print(F"Aprobado!")
else:
    print(f"No esta calificado!")

print(F"\n Condiciones múltiples")
edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puede conducir")
else:
    print("Policia!!")

# un publo de Isla Margarita
if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la Isla Margarita!!")
else:
    print("Paga a la policía y te deja conducir!!")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("Venga que hay que streamer!!")

print("\n Anadir condicionales")
edad = 20
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quedate en casa")
else:
    print("No puedes entrar a la discoteca")

## Mas facil
if edad < 18:
    print("No puedes entrar a la discoteca")
elif tiene_dinero:
    print("Puedes ir a la discoteca")
else:
    print("Quedate en casa")

# Ten en cuenta que hay valores que al usarlos como condiciones
# en Python son evaluados como verdaderos o falsos
# por ejemplo, el número 5, es True
numero = 5
if numero: # True
  print("El número no es cero")

# Pero el número 0 se evalúa como False
numero = 0
if numero: # False
  print("Aquí no entrará nunca")

# También el valor vacío "" se evalúa como False
nombre = ""
if nombre:
  print("El nombre no es vacío")

# ¡Ten cuidado con no confundir la asignación = con la comparación ==!
numero = 3 #  asignación
es_el_tres = numero == 3 # comparación

if es_el_tres:
  print("El número es 3")

# A veces podemos crear condicionales en una sola línea usando
# las ternarias, es una forma concisa de un if-else en una línea de código
print("\nLa condición ternaria:")
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
print("\nEjercicio 1: Cual numero es mayor")
numero1 = input("Ingresa el primer numero")
numero2 = input("Ingresa el segundo numero")

mensaje = "El primer numero es mayor" if numero1 > numero2 else "El segundo numero es mayor"
print(mensaje)


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
print("\nEjercicio 2: Calculadora")
numero1 = int(input("Ingresa el primer numero"))
numero2 = int(input("Ingresa el segundo numero"))
operacion = input("Ingresa una operacion (+, -, *, /)")


if operacion == "+":
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "-":
    resultado = numero1 - numero2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "*":
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicacion es: {resultado}")
elif operacion == "/":
    resultado = numero / numero2
    print(f"El resultado de la division es: {resultado}")
else:
    print(f"La opreción es incorrecta.")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
print("\nEjercicio 3: Año bisiesto")

anno = int(input("Ingrese un año para saber si es bisiesto"))

if (anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0)):
    print(f"{anno} es bisiesto")
else:
    print(f"{anno} no es bisiesto")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)

print("\nEjercicio 4: Categorizar edades")

edad = int(input("Ingrese una edad"))
if edad >= 0 and edad <= 2:
    print("Es un bebé")
elif edad >= 3 and edad <= 12:
    print("Es un niño")
elif edad >= 13 and edad <= 17:
    print("Es un adolecente")
elif edad >= 18 and edad <= 64:
    print("Es un adulto")
else:
    print("Edad incorrecta, debe ingresar un valor entre 0 y 64")



