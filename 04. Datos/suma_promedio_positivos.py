def suma_y_promedio(lista, N):
    suma = 0
    count = 0

    for i in range(N):
        if lista[i] > 0:
            suma += lista[i]
            count += 1

    if count == 0:
        promedio = 0
    else:
        promedio = float(int((suma / count) * 100)) / 100

    return suma, promedio

n = int(input())
lista = []

for _ in range(n):
    lista.append(int(input()))

suma, promedio = suma_y_promedio(lista, n)

print(f"La suma es {suma}")
print(f"El promedio es {promedio:.2f}")
