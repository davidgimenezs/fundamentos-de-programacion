n = int(input())
palabras = []

for _ in range(n):
    palabra = input().strip()
    palabras.append(palabra)

palabras.sort()

for palabra in palabras:
    print(palabra)