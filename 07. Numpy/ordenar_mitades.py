import numpy as np

dimensiones = input().split()
m = int(dimensiones[0])
n = int(dimensiones[1])

elementos = list(map(int, input().split()))

matriz = np.array(elementos).reshape(m, n)

mitad_superior = m // 2
fila_media = None

if m % 2 != 0:
    fila_media = m // 2

elementos_sup = matriz[:mitad_superior].flatten()
elementos_sup.sort()
matriz_sup = elementos_sup.reshape(mitad_superior, n)

if fila_media is not None:
    elementos_inf = matriz[fila_media+1:].flatten()
    elementos_inf.sort()
    elementos_inf = elementos_inf[::-1]
    matriz_inf = elementos_inf.reshape(m-fila_media-1, n)
    
    matriz = np.vstack((matriz_sup, matriz[fila_media:fila_media+1], matriz_inf))
else:
    elementos_inf = matriz[mitad_superior:].flatten()
    elementos_inf.sort()
    elementos_inf = elementos_inf[::-1]
    matriz_inf = elementos_inf.reshape(m-mitad_superior, n)
    
    matriz = np.vstack((matriz_sup, matriz_inf))

for i in range(m):
    for j in range(n):
        print(matriz[i, j], end=" ")
    print()