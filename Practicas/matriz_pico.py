import random

def validar_dimensiones():
    """Valida y obtiene las dimensiones M y N de la matriz"""
    while True:
        try:
            M = int(input("Ingrese el número de filas (M): "))
            if M <= 0:
                print("Error: M debe ser un número entero positivo")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número entero válido")
    
    while True:
        try:
            N = int(input("Ingrese el número de columnas (N): "))
            if N <= 0:
                print("Error: N debe ser un número entero positivo")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número entero válido")
    
    return M, N

def generar_matriz(M, N):
    """Genera una matriz M x N con valores aleatorios entre 1 y 50"""
    matriz = []
    for i in range(M):
        fila = []
        for j in range(N):
            fila.append(random.randint(1, 50))
        matriz.append(fila)
    return matriz

def es_pico(matriz, i, j):
    """Determina si la posición (i,j) corresponde a un pico"""
    M = len(matriz)
    N = len(matriz[0])
    valor_actual = matriz[i][j]
    
    # Definir las direcciones de los vecinos (arriba, abajo, izquierda, derecha)
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for di, dj in direcciones:
        ni, nj = i + di, j + dj
        # Verificar si el vecino está dentro de los límites
        if 0 <= ni < M and 0 <= nj < N:
            # Si algún vecino es mayor o igual, no es pico
            if matriz[ni][nj] >= valor_actual:
                return False
    
    return True

def obtener_picos(matriz):
    """Obtiene todas las posiciones que corresponden a picos"""
    M = len(matriz)
    N = len(matriz[0])
    picos = []
    
    for i in range(M):
        for j in range(N):
            if es_pico(matriz, i, j):
                picos.append((i, j, matriz[i][j]))  # (fila, columna, valor)
    
    return picos

def ordenar_picos(picos):
    """Ordena las posiciones de picos en orden no-descendente por valor"""
    # Ordenar por valor (tercer elemento de la tupla) en orden no-descendente
    picos_ordenados = sorted(picos, key=lambda x: x[2])
    return picos_ordenados

def mostrar_matriz(matriz):
    """Muestra la matriz en pantalla"""
    print("\nMatriz generada:")
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:3}", end=" ")
        print()

def mostrar_picos(picos_ordenados):
    """Muestra las posiciones de los picos ordenadas"""
    print("\nPosiciones de los picos (orden no-descendente por valor):")
    posiciones = []
    for i, j, valor in picos_ordenados:
        posiciones.append(f"({i}, {j})")
    
    print(" ".join(posiciones))
    
    print("\nDetalle de los picos:")
    for i, j, valor in picos_ordenados:
        print(f"Posición ({i}, {j}): valor = {valor}")

"""Función principal del programa"""
print("=== DETECTOR DE PICOS EN MATRIZ ===")

# Validar dimensiones
M, N = validar_dimensiones()

# Generar matriz aleatoria
matriz = generar_matriz(M, N)

# Mostrar matriz
mostrar_matriz(matriz)

# Obtener picos
picos = obtener_picos(matriz)

# Ordenar picos
picos_ordenados = ordenar_picos(picos)

# Mostrar resultados
mostrar_picos(picos_ordenados)