def maximo(lista, N):
    mayor = lista[0]
    for i in range(1, N):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

def minimo(lista, N):
    menor = lista[0]
    for i in range(1, N):
        if lista[i] < menor:
            menor = lista[i]
    return menor

n = int(input())
lista = []

for _ in range(n):
    lista.append(int(input()))

print(f"El Mayor es {maximo(lista, n)}")
print(f"El Menor es {minimo(lista, n)}")