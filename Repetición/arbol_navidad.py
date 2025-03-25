def imprimir_arbol():
    n = int(input())
    print(f"Arbol de {n} filas:")
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

imprimir_arbol()