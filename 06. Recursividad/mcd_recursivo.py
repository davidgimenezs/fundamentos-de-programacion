def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())
print(f"El MCD resultante es {mcd(a, b)}")