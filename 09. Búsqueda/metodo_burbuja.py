import numpy as np

def recibe(A):
    for i in range(len(A)):
        A[i] = int(input())
        
def burbuja(A):
    n = len(A)
    imprime(A)
    
    for recorrido in range(n-1):
        for i in range(n-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
        imprime(A)
    
def imprime(A):
    for elem in A:
        print(elem, end="\t")
    print()
    
tamano = 10
arreglo = np.zeros(tamano, dtype=int)

recibe(arreglo)
burbuja(arreglo)