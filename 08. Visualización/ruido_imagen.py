import numpy as np
import matplotlib.pyplot as plt

imagen_con_ruido = np.loadtxt('imagen_con_ruido.csv', delimiter=',')

filtrada = np.zeros_like(imagen_con_ruido)

filas, columnas = imagen_con_ruido.shape

for i in range(1, filas - 1):
    for j in range(1, columnas - 1):
        vecindad = imagen_con_ruido[i-1:i+2, j-1:j+2]
        promedio = np.mean(vecindad)
        filtrada[i, j] = promedio

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagen_con_ruido, cmap='gray')
plt.title("Imagen con ruido")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtrada, cmap='gray')
plt.title("Imagen filtrada")
plt.axis('off')

plt.tight_layout()
plt.show()
