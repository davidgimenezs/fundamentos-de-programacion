import numpy as np
import random

random.seed(10)

n = int(input())

cedulas = []
numeros_aleatorios = []

print("Ingrese los números de cédula de los", n, "alumnos:")
for i in range(n):
    cedula = input()
    cedulas.append(cedula)
    
    numero_aleatorio = random.randint(1, 100)
    numeros_aleatorios.append(numero_aleatorio)

print()
print("Asignación inicial:")
for i in range(n):
    print(f"CI: {cedulas[i]}\tNúmero al azar: {numeros_aleatorios[i]}")

indices = np.arange(n)

indices_ordenados = indices[np.argsort(numeros_aleatorios)]

cedulas_ordenadas = [cedulas[i] for i in indices_ordenados]
numeros_ordenados = sorted(numeros_aleatorios)

print()
print("Asignación ordenada por números aleatorios:")
for i in range(n):
    print(f"CI: {cedulas_ordenadas[i]}\tNúmero al azar: {numeros_ordenados[i]}")

print("Ci", end=" ")
for ci in cedulas_ordenadas:
    print(ci, end=" ")
print()
print("Azar", end=" ")
for num in numeros_ordenados:
    print(num, end=" ")
print()