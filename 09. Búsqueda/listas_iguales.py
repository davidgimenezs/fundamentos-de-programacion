def tienen_mismos_elementos(lista1, lista2):
    return sorted(lista1) == sorted(lista2)

N = int(input())

print()
lista1 = []
for i in range(N):
    numero = int(input())
    lista1.append(numero)

print()
lista2 = []
for i in range(N):
    numero = int(input())
    lista2.append(numero)

if tienen_mismos_elementos(lista1, lista2):
    print("SI son iguales")
else:
    print("No son iguales")
