import numpy as np

def main():
    n = int(input().strip())
    matriz = np.zeros((n, n), dtype=int)
    
    for i in range(n):
        row_input = list(map(int, input().strip().split()))
        for j in range(n):
            matriz[i, j] = row_input[j]
    
    diagonal_sum = np.trace(matriz)
    
    if diagonal_sum % 2 == 0:
        for j in range(n):
            matriz[:, j] = np.sort(matriz[:, j])[::-1]
    else:
        for j in range(n):
            matriz[:, j] = np.sort(matriz[:, j])
    
    for i in range(n):
        print(' '.join(map(str, matriz[i])))