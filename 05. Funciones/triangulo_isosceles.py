def t_isosceles(n):
    for i in range(1, n + 1):
        espacios = ' ' * (n - i)
        asteriscos = '*' * (2 * i - 1)
        print(espacios + asteriscos)

n = int(input())
t_isosceles(n)
