def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def combinaciones(m, n):
    if m > n:
        return 0
    return factorial(n) // (factorial(m) * factorial(n - m))

opcion = int(input())
n = int(input())

if opcion == 1:
    print(factorial(n))
elif opcion == 2:
    m = int(input())
    print(combinaciones(m, n))