import numpy as np
import matplotlib.pyplot as plt
import random

def generar_puntos(n):
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    return x, y

def calcular_distancia(x, y):
    return x**2 + y**2

def visualizar_monte_carlo(n):
    x, y = generar_puntos(n)
    
    distancias = calcular_distancia(x, y)
    
    dentro_circulo = distancias <= 1
    
    n_dentro = np.sum(dentro_circulo)
    n_fuera = n - n_dentro
    
    pi_estimado = (n_dentro / n) * 4
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    cuadrado = plt.Rectangle((-1, -1), 2, 2, fill=False, color='black', linewidth=2)
    ax.add_patch(cuadrado)
    
    circulo = plt.Circle((0, 0), 1, fill=False, color='black', linewidth=2)
    ax.add_patch(circulo)
    
    ax.scatter(x[dentro_circulo], y[dentro_circulo], color='blue', s=5, alpha=0.6, label=f'Dentro: {n_dentro}')
    ax.scatter(x[~dentro_circulo], y[~dentro_circulo], color='red', s=5, alpha=0.6, label=f'Fuera: {n_fuera}')
    
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_title(f'π ≈ {pi_estimado:.6f}')
    ax.legend(loc='upper right')
    
    plt.show()
    
    return n_dentro, pi_estimado

def imprimirMensajeOpcion2(n):
    print("Se generaron", n, "números dentro del círculo")

def imprimirMensajeOpcion3(pi):
    print(f"El valor estimado de pi es {pi:.4f}")

def estimarPi(n):
    random.seed(42)
    dentro = 0
    
    for i in range(n):
        x = random.random()
        y = random.random()
        
        if x*x + y*y <= 1:
            dentro += 1
    
    pi_estimado = 4 * dentro / n
    return dentro, pi_estimado

try:
    opcion = int(input())
    
    if opcion == 1:
        random.seed(42)
        for i in range(10):
            num = random.random()
            if i < 9:
                print(f"{num:.4f}", end=" ")
            else:
                print(f"{num:.4f}")
            
    elif opcion == 2:
        random.seed(42)
        n = int(input("Ingresa la cantidad de puntos a generar: "))
        
        dentro, _ = estimarPi(n)
        imprimirMensajeOpcion2(dentro)
            
    elif opcion == 3:
        n = int(input("Ingresa la cantidad de puntos para estimar π: "))
        _, pi = estimarPi(n)
        imprimirMensajeOpcion3(pi)
    
    else:
        print("Opción no válida. Por favor selecciona 1, 2 o 3.")
        
except ValueError:
    print("Error: Por favor ingresa un número entero.")