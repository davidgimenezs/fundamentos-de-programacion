import numpy as np

n = int(input())

# Creamos una matriz de 3 filas y n columnas
fechas = np.zeros((3, n), dtype=int)

# Leemos las fechas y las almacenamos en la matriz
for j in range(n):
    for i in range(3):
        fechas[i][j] = int(input())

# Creamos un array auxiliar para ordenar
indices = np.zeros(n, dtype=int)
for i in range(n):
    indices[i] = i

# Ordenamos los índices basados en la combinación de año, mes y día
for i in range(n):
    for j in range(i + 1, n):
        # Si el año es mayor, intercambiamos
        if fechas[0][indices[i]] > fechas[0][indices[j]]:
            indices[i], indices[j] = indices[j], indices[i]
        # Si el año es igual, comparamos los meses
        elif fechas[0][indices[i]] == fechas[0][indices[j]]:
            if fechas[1][indices[i]] > fechas[1][indices[j]]:
                indices[i], indices[j] = indices[j], indices[i]
            # Si el mes es igual, comparamos los días
            elif fechas[1][indices[i]] == fechas[1][indices[j]]:
                if fechas[2][indices[i]] > fechas[2][indices[j]]:
                    indices[i], indices[j] = indices[j], indices[i]

# Creamos la matriz ordenada
fechas_ordenadas = np.zeros((3, n), dtype=int)
for i in range(3):
    for j in range(n):
        fechas_ordenadas[i][j] = fechas[i][indices[j]]

# Imprimimos el resultado ordenado
for i in range(3):
    for j in range(n):
        print(fechas_ordenadas[i][j], end="    ")
    print()