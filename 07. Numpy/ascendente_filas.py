import numpy as np

def validar():
    while True:
        try:
            valor = int(input())
            if valor > 0:
                return valor
        except ValueError:
            pass

def tiene_secuencia_ascendente(fila):
    contador = 1
    for i in range(1, len(fila)):
        if fila[i] > fila[i-1]:
            contador += 1
            if contador >= 3:
                return True
        else:
            contador = 1
    return False

m = validar()
n = validar()

matriz = np.zeros((m, n), dtype=int)
for i in range(m):
    for j in range(n):
        matriz[i][j] = validar()

columnas_con_secuencia = 0
columnas_encontradas = []

for j in range(n):
    if tiene_secuencia_ascendente(matriz[:, j]):
        columnas_con_secuencia += 1
        columnas_encontradas.append(j+1)

if columnas_con_secuencia == 0:
    print(0)
else:
    print(columnas_con_secuencia)
    for columna in columnas_encontradas:
        print(columna)