def generar_diamante(n):
    for i in range(1, n + 1):
        espacios = '-' * (n - i)
        asteriscos = '*' * (2 * i - 1)
        print(espacios + asteriscos)
    
    for i in range(n - 1, 0, -1):
        espacios = '-' * (n - i)
        asteriscos = '*' * (2 * i - 1)
        print(espacios + asteriscos)

n = int(input())
generar_diamante(n)
