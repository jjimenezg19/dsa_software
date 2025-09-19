"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud.

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""
from calendar import different_locale


def battle(lista_a, lista_b):
    a_copy = lista_a[:]
    b_copy = lista_b[:]
    for i in range(len(a_copy) - 1):
        if a_copy[i] > b_copy[i]:
            diff = a_copy[i] - b_copy[i]
            a_copy[i + 1] +=  diff
        elif a_copy[i] < b_copy[i]:
            diff = b_copy[i] - a_copy[i]
            b_copy[i + 1] +=  diff

    if a_copy[-1] > b_copy[-1]:
        return f"{a_copy[-1] - b_copy[-1]}a"
    elif a_copy[-1] < b_copy[-1]:
        return f"{b_copy[-1] - a_copy[-1]}b"
    else:
        return "X"

lista_a = [10, 9, 9, 3]
lista_b = [4, 4, 4, 12]
resultado = battle(lista_a, lista_b)
print(resultado)


def battle(a, b):
    for i in range(len(a) - 1):
        diff = a[i] - b[i]
        if diff > 0:
            a[i + 1] += diff
        elif diff < 0:
            b[i + 1] += -diff

    diff = a[-1] - b[-1]
    if diff > 0:
        return f"{diff}a"
    elif diff < 0:
        return f"{-diff}b"
    else:
        return "x"