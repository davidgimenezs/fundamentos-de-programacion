import random

SEMILLA = 42

def imprimirMensaje(n, a, b):
    print(f"Se generaron {n} números entre {a} y {b}")

opcion = int(input())

if opcion == 1:
    random.seed(SEMILLA)
    a = int(input())
    b = int(input())
    random_numbers = [random.randint(a, b) for _ in range(10)]
    print(" ".join(map(str, random_numbers)))

if opcion == 2:
    random.seed(SEMILLA)
    a = int(input())
    b = int(input())
    accu = 0
    random_numbers = [random.randint(1, 100) for _ in range(100)]
    for num in random_numbers:
        if a <= num <= b:
            accu += 1
    imprimirMensaje(accu, a, b)

if opcion == 3:
    random.seed(SEMILLA)
    n = int(input())
    random_numbers = [random.randint(1, 10) for _ in range(n)]
    count_1_3 = sum(1 for num in random_numbers if 1 <= num <= 3)
    count_4_6 = sum(1 for num in random_numbers if 4 <= num <= 6)
    count_7_9 = sum(1 for num in random_numbers if 7 <= num <= 9)

    print(f"Se generaron {count_1_3} números entre 1 y 3")
    print(f"Se generaron {count_4_6} números entre 4 y 6")
    print(f"Se generaron {count_7_9} números entre 7 y 9")