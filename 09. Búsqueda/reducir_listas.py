def generar_lista_comprimida():
    N = int(input())
    L1 = []

    for _ in range(N):
        L1.append(int(input()))

    unicos = sorted(set(L1))

    L2 = []
    for valor in unicos:
        L2.append(valor)
        L2.append(L1.count(valor))

    print(L2)

generar_lista_comprimida()
