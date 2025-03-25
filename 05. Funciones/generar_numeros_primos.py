def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generar_primos(N):
    return [num for num in range(2, N + 1) if es_primo(num)]

N = int(input())
primos = generar_primos(N)
print(" ".join(map(str, primos)))
