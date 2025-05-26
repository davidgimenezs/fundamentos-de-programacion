import numpy as np

N = int(input())

array_A = np.array(list(map(int, input().split())))
array_B = np.array(list(map(int, input().split())))

resultado = array_A + array_B

print(resultado.tolist())