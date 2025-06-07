"""
===============================================================================
                    ANÁLISIS DE PENDIENTES LOCALES EN MATRICES
===============================================================================

DESCRIPCIÓN DEL PROBLEMA:
------------------------
Para este ejercicio, se desea analizar una matriz de números enteros y encontrar 
aquellas posiciones que presentan una pendiente local alta. 

DEFINICIÓN DE PENDIENTE LOCAL:
La pendiente local de una celda se define como la diferencia entre el valor de 
esa celda y el promedio de sus vecinos adyacentes (solo se consideran los vecinos 
directo: superior, inferior, izquierdo y derecho). 

CASOS ESPECIALES:
En el caso de las posiciones ubicadas en los bordes de la matriz (primera fila, 
primera columna, última fila, última columna), se deberán considerar solamente 
los vecinos existentes.

OBJETIVO:
---------
Determinar las cinco posiciones con mayor pendiente local de la matriz, junto 
con su valor de pendiente. En caso de que existan menos de cinco valores únicos 
de pendiente, se deben mostrar todas las posiciones posibles ordenadas de mayor 
a menor según el valor de la pendiente.

===============================================================================
                            REQUISITOS DEL PROGRAMA
===============================================================================

1. VALIDACIÓN DE ENTRADA:
   ● Solicitar al usuario dos números enteros positivos M y N, correspondientes 
     a las dimensiones de la matriz
   ● Validar que ambos sean mayores a 1

2. GENERACIÓN DE MATRIZ:
   ● Generar una matriz de M filas por N columnas
   ● Valores generados aleatoriamente en el rango de [10, 100]

3. CÁLCULO DE PENDIENTES:
   ● Calcular la pendiente local para cada celda de la matriz

4. MOSTRAR RESULTADOS:
   ● La matriz generada
   ● Las cinco posiciones (i, j) con mayor pendiente local y el valor de 
     dicha pendiente, ordenadas de mayor a menor

===============================================================================
                            EJEMPLO DE SALIDA ESPERADA
===============================================================================

Matriz generada:
+----+----+----+----+
| 14 | 22 |  9 | 33 |
+----+----+----+----+
| 17 |  8 | 44 | 10 |
+----+----+----+----+
| 11 | 23 | 31 |  6 |
+----+----+----+----+

Top 5 pendientes locales:
┌─────────────┬────────────┐
│  Posición   │ Pendiente  │
├─────────────┼────────────┤
│   (1, 2)    │   24.75    │
│   (0, 3)    │   13.0     │
│   (2, 2)    │   11.0     │
│   (1, 0)    │   10.0     │
│   (2, 1)    │    9.5     │
└─────────────┴────────────┘
===============================================================================
                            CRITERIOS DE EVALUACIÓN
===============================================================================

┌─────────────────────────────────────────────────────────────────┬─────────┐
│                              ÍTEM                               │ PUNTAJE │
├─────────────────────────────────────────────────────────────────┼─────────┤
│ Validación de las dimensiones de la matriz                      │   10%   │
├─────────────────────────────────────────────────────────────────┼─────────┤
│ Generación aleatoria de la matriz                               │   10%   │
├─────────────────────────────────────────────────────────────────┼─────────┤
│ Cálculo correcto de los vecinos válidos para cada celda         │   15%   │
├─────────────────────────────────────────────────────────────────┼─────────┤
│ Cálculo de la pendiente local para cada posición                │   15%   │
├─────────────────────────────────────────────────────────────────┼─────────┤
│ Almacenamiento correcto de posiciones con sus pendientes        │   10%   │
├─────────────────────────────────────────────────────────────────┼─────────┤
│ Selección y orden correcto de las cinco mayores pendientes      │   20%   │
├─────────────────────────────────────────────────────────────────┼─────────┤
│ Impresión clara y estructurada de resultados (con formato)      │   10%   │
├─────────────────────────────────────────────────────────────────┼─────────┤
│ Uso adecuado de funciones (mínimo dos funciones definidas)      │   10%   │
├─────────────────────────────────────────────────────────────────┼─────────┤
│ Penalización por errores de sintaxis                            │ -5% c/u │
└─────────────────────────────────────────────────────────────────┴─────────┘

                                 TOTAL: 100%

===============================================================================
                               RECORDATORIOS IMPORTANTES
===============================================================================

⚠️  ADVERTENCIAS:
   ● Los estudiantes que tengan soluciones similares llevarán 0%
   ● La evaluación será realizada manualmente

📝 ENTREGA:
   ● Se puede resolver el ejercicio en el VPL o en el VS CODE
   ● Recuerde guardar cada paso en el VPL

===============================================================================
"""


import numpy as np

def validar_Numero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False
    
def validar_Positivo(numero):
    if validar_Numero(numero):
        numero = int(numero)
        if numero > 1:
            print("¡La entrada ingresada es correcta!")
            return numero
        else:

            print("La entrada ingresada NO es correcta (El número debe ser entero y positivo)")
    else:
        print("La entrada ingresada NO es correcta (Debe se un número)")    
        
def generar_Aleatorio(matriz, m, n):
    i=0
    j=0
    for i in range(m):
        for j in range(n):
            matriz[i][j] = np.random.randint(10,100)
    
'''
Esta funcion va a identificar con un return la posicion relativa, diferencia esquinas de pared de intermedio
|-------------------|                           Leyenda:
| 1  ...  6  ...  2 |         1. ESQUINA TL     5. IZQUIERDA     9. INTERMEDIO
| -       -       - |         2. ESQUINA TR     6. TECHO
| 5  ...  9  ...  7 |         3. ESQUINA BL     7. DERECHA
| -       -       - |         4. ESQUINA BR     8. PISO
| 3  ...  8  ...  4 |         
|-------------------|         
'''
def identificar_Posicion(matriz, m, n, auxiliar):
    for i in range(m):
        for j in range(n):
            if i == 0:
                if j == 0:
                    #print(f"{matriz[i][j]} Es una esquina TL.")
                    auxiliar[i][j] = 1
                elif j == n-1:
                    #print(f"{matriz[i][j]} Es una esquina TR.")
                    auxiliar[i][j] = 2
                elif j > 0 and j < n-1:
                    #print(f"{matriz[i][j]} Es una posición sobre el techo")
                    auxiliar[i][j] = 6

            elif j == 0:
                if i == m-1:
                    #print(f"{matriz[i][j]} Es una esquina BL.")
                    auxiliar[i][j] = 3
                elif i > 0 and i < m-1:
                    #print(f"{matriz[i][j]} Es una posición sobre la pared izquierda")
                    auxiliar[i][j] = 5

            elif i == m-1:
                if j == n-1:
                    #print(f"{matriz[i][j]} Es una esquina BR.")
                    auxiliar[i][j] = 4
                else:
                    #print(f"{matriz[i][j]} Es una posición sobre el piso")
                    auxiliar[i][j] = 8

            elif j == n-1:
                #print(f"{matriz[i][j]} Es una posición sobre la pared derecha")
                auxiliar[i][j] = 7
            
            else:
               #print(f"{matriz[i][j]} Es una posicion intermedia.")
                auxiliar[i][j] = 93

def sumar_Posiciones(matriz, i, j, temp):
    if temp == 1:
        up = 0
        down = matriz[i+1][j]
        left = 0
        right = matriz[i][j+1]
    if temp == 2:
        up = 0
        down = matriz[i+1][j]
        left = matriz[i][j-1]
        right = 0
    if temp == 3:
        up = matriz[i-1][j]
        down = 0
        left = 0
        right = matriz[i][j+1]
    if temp == 4:
        up = matriz[i-1][j]
        down = 0
        left = matriz[i][j-1]
        right = 0
    if temp == 5:
        up = matriz[i-1][j]
        down = matriz[i+1][j]
        left = 0
        right = matriz[i][j+1]
    if temp == 6:
        up = 0
        down = matriz[i+1][j]
        left = matriz[i][j-1]
        right = matriz[i][j+1]
    if temp == 7:
        up = matriz[i-1][j]
        down = matriz[i+1][j]
        left = matriz[i][j-1]
        right = 0
    if temp == 8:
        up = matriz[i-1][j]
        down = 0
        left = matriz[i][j-1]
        right = matriz[i][j+1]
    if temp == 9:
        up = matriz[i-1][j]
        down = matriz[i+1][j]
        left = matriz[i][j-1]
        right = matriz[i][j+1]

    return up, down, left, right


def promedio_Matriz(matriz, m, n, auxiliar, promedio):
    for i in range(m):
        for j in range(n):
            if auxiliar[i][j] == 1:
                #sumar derecha + abajo
                up, down, left, right = sumar_Posiciones(matriz, i, j, 1)
                promedio[i][j] = (right + down)/2
            elif auxiliar[i][j] == 2:
                #sumar izquierda + abajo
                up, down, left, right = sumar_Posiciones(matriz, i, j, 2)
                promedio[i][j] = (left + down)/2
            elif auxiliar[i][j] == 3:
                #sumar arriba + derecha
                up, down, left, right = sumar_Posiciones(matriz, i, j, 3)
                promedio[i][j] = (up + right)/2
            elif auxiliar[i][j] == 4:
                #sumar arriba + izquierda
                up, down, left, right = sumar_Posiciones(matriz, i, j, 4)
                promedio[i][j] = (up + left)/2
            elif auxiliar[i][j] == 5:
                #sumar arriba + abajo + derecha
                up, down, left, right = sumar_Posiciones(matriz, i, j, 5)
                promedio[i][j] = (up + down + right)/3
            elif auxiliar[i][j] == 6:
                #sumar izquierda + derecha + abajo
                up, down, left, right = sumar_Posiciones(matriz, i, j, 6)
                promedio[i][j] = (left + right + down)/3
            elif auxiliar[i][j] == 7:
                #sumar arriba + abajo + izquierda
                up, down, left, right = sumar_Posiciones(matriz, i, j, 7)
                promedio[i][j] = (up + down + left)/3
            elif auxiliar[i][j] == 8:
                #sumar arriba + izquierda + derecha
                up, down, left, right = sumar_Posiciones(matriz, i, j, 8)
                promedio[i][j] = (up + left + right)/3
            elif auxiliar[i][j] == 9:
                #sumar arriba + izquierda + derecha + abajo
                up, down, left, right = sumar_Posiciones(matriz, i, j, 9)
                promedio[i][j] = (up + left + right + down)/4

def pendiente_Matriz(matriz, m, n, auxiliar):
    for i in range(m):
        for j in range(n):
            pendiente[i][j] = matriz[i][j] - promedio[i][j]

def maximos_Pendientes(pendiente, m, n, maximos, posiciones_i, posiciones_j):
    for i in range(m):
        for j in range(n):
            for k in range(5):
                if pendiente[i][j] > maximos[k]:
                    for l in range(4, k, -1):
                        maximos[l] = maximos[l-1]
                        posiciones_i[l] = posiciones_i[l-1]
                        posiciones_j[l] = posiciones_j[l-1]
                    
                    maximos[k] = pendiente[i][j]
                    posiciones_i[k] = i
                    posiciones_j[k] = j
                    break

while True:
    print("╔══════════════════════════════╗")
    print("║     Ingrese el numero de     ║")
    print("║      filas de la matriz      ║")
    print(f"╚══════════════════════════════╝")

    bandera = True
    while bandera == True:
        m = input()
        if validar_Positivo(m) and validar_Numero(m):
            print()
            m = int(m)
            bandera = False

    print("╔══════════════════════════════╗")
    print("║     Ingrese el numero de     ║")
    print("║     columnas de la matriz    ║")
    print(f"╚══════════════════════════════╝")

    bandera = True
    while bandera == True:
        n = input()
        if validar_Positivo(n) and validar_Numero(n):
            n = int(n)
            bandera = False

    bandera = True
    while bandera == True:

        matriz = np.zeros((m,n), dtype=int)
        auxiliar = np.zeros((m,n), dtype=int)
        pendiente = np.zeros((m,n), dtype=float)
        promedio = np.zeros((m,n), dtype=float)
        maximos = np.zeros((5), dtype=float)
        posiciones_i = np.zeros((5), dtype=int)
        posiciones_j = np.zeros((5), dtype=int)

        generar_Aleatorio(matriz, m, n)
        #matriz = [(14, 22, 9, 33),(17, 8, 44, 10),(11, 23, 31, 6)]
        
        print()
        print("╔══════════════════════════════╗")
        print("║    La matriz generada es     ║")
        if m >= 10 or n >= 10:
            if m >= 10 and n >= 10:
                print(f"║         de {m} x {n}           ║")
            else:
                print(f"║          de {m} x {n}           ║")
        if m < 10 and n < 10:
            print(f"║          de {m} x {n}            ║")
        print(f"╚══════════════════════════════╝")
        print(matriz)

        identificar_Posicion(matriz, m, n, auxiliar)
        promedio_Matriz(matriz, m, n, auxiliar, promedio)
        pendiente_Matriz(matriz, m, n, promedio)
        maximos_Pendientes(pendiente, m, n, maximos, posiciones_i, posiciones_j)

        print()
        print("╔══════════════════════════════╗")
        print("║   Top 5 pendientes locales   ║")
        print("╠═══╦══════════╦═══════════════╣")
        print("║ N ║ Posicion ║   Pendiente   ║")
        print("╠═══╬══════════╬═══════════════╣")

        for i in range(5):
            if maximos[i] < 10:
                print(f"║ {i+1} ║  ({posiciones_i[i]}, {posiciones_j[i]})  ║     {maximos[i]:.2f}      ║")
            elif maximos[i] >= 10:
                print(f"║ {i+1} ║  ({posiciones_i[i]}, {posiciones_j[i]})  ║     {maximos[i]:.2f}     ║")
            elif maximos[i] >= 100:
                print(f"║ {i+1} ║  ({posiciones_i[i]}, {posiciones_j[i]})  ║     {maximos[i]:.2f}    ║")

        print(f"╚═══╩══════════╩═══════════════╝")
        print("--------------------------------")

        bandera = False