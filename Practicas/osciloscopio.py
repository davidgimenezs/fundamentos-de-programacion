import numpy as np
import matplotlib.pyplot as plt

t1 = float(input("Ingrese el valor mínimo del eje X (t1): "))
t2 = float(input("Ingrese el valor máximo del eje X (t2): "))

while t1 >= t2:
    print("Error: t1 debe ser menor que t2")
    t1 = float(input("Ingrese el valor mínimo del eje X (t1): "))
    t2 = float(input("Ingrese el valor máximo del eje X (t2): "))

def f(atenuacion, frecuencia, T):
    t = np.linspace(t1, t2, 1000)
    resultado = np.exp(-atenuacion * t) * np.sin(2 * np.pi * frecuencia * t + T)
    return t, resultado

t, y1 = f(0.1, 50, 0)
t, y2 = f(0.3, 150, 0)

plt.figure(figsize=(10, 6))
plt.plot(t, y1, label='A=0.1, f=50', color='blue')
plt.plot(t, y2, label='A=0.3, f=150', color='orange')
plt.title('Osciloscopio')
plt.xlabel('Tiempo [s]')
plt.ylabel('Tensión [V]')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()