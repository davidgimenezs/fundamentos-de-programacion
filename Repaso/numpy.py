# TUTORIAL COMPLETO DE NUMPY
# Computación numérica eficiente con Python
# Autor: David
# Fecha: Mayo 2025

import numpy as np
import time
import matplotlib.pyplot as plt
from datetime import datetime

# Configuración para mostrar más decimales cuando sea necesario
np.set_printoptions(precision=3, suppress=True)

print("🔢 BIENVENIDO AL TUTORIAL COMPLETO DE NUMPY")
print("Computación numérica de alto rendimiento con Python")
print("=" * 60)


def seccion_1_introduccion():
    """
    SECCIÓN 1: Introducción a NumPy
    - ¿Qué es NumPy y por qué usarlo?
    - Comparación con listas de Python
    - Instalación y configuración
    """
    print("\n📚 SECCIÓN 1: INTRODUCCIÓN A NUMPY")
    print("=" * 50)
    
    print("💡 ¿Qué es NumPy?")
    print("NumPy (Numerical Python) es la biblioteca fundamental para")
    print("computación científica en Python. Proporciona:")
    print("• Arrays N-dimensionales eficientes")
    print("• Funciones matemáticas optimizadas")
    print("• Herramientas de álgebra lineal")
    print("• Capacidades de broadcasting")
    print("• Integración con C/C++ y Fortran")
    
    print("\n⚡ Ventajas de NumPy vs Listas de Python:")
    
    # Comparación de rendimiento
    print("\n🏃‍♂️ Prueba de velocidad - Suma de 1 millón de números:")
    
    # Lista de Python
    lista_python = list(range(1000000))
    inicio = time.time()
    suma_python = sum(lista_python)
    tiempo_python = time.time() - inicio
    
    # Array de NumPy
    array_numpy = np.arange(1000000)
    inicio = time.time()
    suma_numpy = np.sum(array_numpy)
    tiempo_numpy = time.time() - inicio
    
    print(f"   Lista Python: {tiempo_python:.4f} segundos")
    print(f"   Array NumPy:  {tiempo_numpy:.4f} segundos")
    print(f"   🚀 NumPy es {tiempo_python/tiempo_numpy:.1f}x más rápido!")
    
    # Comparación de memoria
    import sys
    memoria_lista = sys.getsizeof(lista_python[:1000])
    memoria_array = array_numpy[:1000].nbytes
    print(f"\n💾 Uso de memoria (1000 elementos):")
    print(f"   Lista Python: {memoria_lista:,} bytes")
    print(f"   Array NumPy:  {memoria_array:,} bytes")
    print(f"   💡 NumPy usa {memoria_lista/memoria_array:.1f}x menos memoria!")
    
    print("\n✅ Sección 1 completada - ¡NumPy es poderoso!")


def seccion_2_creacion_arrays():
    """
    SECCIÓN 2: Creación de Arrays
    - Diferentes formas de crear arrays
    - Tipos de datos
    - Dimensiones y formas
    """
    print("\n📚 SECCIÓN 2: CREACIÓN DE ARRAYS")
    print("=" * 50)
    
    print("🔨 1. Creación desde listas:")
    # Array 1D
    arr_1d = np.array([1, 2, 3, 4, 5])
    print(f"   Array 1D: {arr_1d}")
    print(f"   Forma: {arr_1d.shape}, Dimensiones: {arr_1d.ndim}")
    
    # Array 2D
    arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\n   Array 2D:\n{arr_2d}")
    print(f"   Forma: {arr_2d.shape}, Dimensiones: {arr_2d.ndim}")
    
    # Array 3D
    arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(f"\n   Array 3D:\n{arr_3d}")
    print(f"   Forma: {arr_3d.shape}, Dimensiones: {arr_3d.ndim}")
    
    print("\n🔨 2. Funciones de creación especiales:")
    
    # Ceros y unos
    ceros = np.zeros((3, 4))
    unos = np.ones((2, 3, 2))
    identidad = np.eye(4)
    
    print(f"   Matriz de ceros (3x4):\n{ceros}")
    print(f"\n   Matriz de unos (2x3x2):\n{unos}")
    print(f"\n   Matriz identidad (4x4):\n{identidad}")
    
    # Rangos y secuencias
    print("\n🔨 3. Rangos y secuencias:")
    secuencia1 = np.arange(0, 10, 2)  # inicio, fin, paso
    secuencia2 = np.linspace(0, 1, 5)  # inicio, fin, cantidad
    secuencia3 = np.logspace(0, 2, 5)  # 10^0 a 10^2, 5 puntos
    
    print(f"   arange(0, 10, 2): {secuencia1}")
    print(f"   linspace(0, 1, 5): {secuencia2}")
    print(f"   logspace(0, 2, 5): {secuencia3}")
    
    # Arrays aleatorios
    print("\n🔨 4. Arrays aleatorios:")
    np.random.seed(42)  # Para reproducibilidad
    aleatorio_uniforme = np.random.random((2, 3))
    aleatorio_normal = np.random.normal(0, 1, (2, 3))
    aleatorio_enteros = np.random.randint(1, 10, (2, 3))
    
    print(f"   Random uniforme [0,1):\n{aleatorio_uniforme}")
    print(f"\n   Random normal (μ=0, σ=1):\n{aleatorio_normal}")
    print(f"\n   Random enteros [1,10):\n{aleatorio_enteros}")
    
    # Tipos de datos
    print("\n🔨 5. Tipos de datos:")
    arr_int = np.array([1, 2, 3], dtype=np.int32)
    arr_float = np.array([1, 2, 3], dtype=np.float64)
    arr_complex = np.array([1+2j, 3+4j])
    arr_bool = np.array([True, False, True])
    
    print(f"   Enteros int32: {arr_int} - tipo: {arr_int.dtype}")
    print(f"   Flotantes float64: {arr_float} - tipo: {arr_float.dtype}")
    print(f"   Complejos: {arr_complex} - tipo: {arr_complex.dtype}")
    print(f"   Booleanos: {arr_bool} - tipo: {arr_bool.dtype}")
    
    print("\n✅ Sección 2 completada - ¡Arrays creados exitosamente!")


def seccion_3_indexado_slicing():
    """
    SECCIÓN 3: Indexado y Slicing
    - Acceso a elementos
    - Slicing avanzado
    - Indexado booleano
    - Indexado con arrays
    """
    print("\n📚 SECCIÓN 3: INDEXADO Y SLICING")
    print("=" * 50)
    
    # Crear array de ejemplo
    arr = np.arange(20).reshape(4, 5)
    print(f"Array de ejemplo (4x5):\n{arr}")
    
    print("\n🎯 1. Indexado básico:")
    print(f"   arr[0, 0] = {arr[0, 0]} (primera fila, primera columna)")
    print(f"   arr[2, 3] = {arr[2, 3]} (tercera fila, cuarta columna)")
    print(f"   arr[-1, -1] = {arr[-1, -1]} (última fila, última columna)")
    
    print("\n🎯 2. Slicing de filas y columnas:")
    print(f"   Primera fila: arr[0, :] = {arr[0, :]}")
    print(f"   Primera columna: arr[:, 0] = {arr[:, 0]}")
    print(f"   Últimas 2 filas: arr[-2:, :] =\n{arr[-2:, :]}")
    print(f"   Columnas del medio: arr[:, 1:4] =\n{arr[:, 1:4]}")
    
    print("\n🎯 3. Slicing con pasos:")
    print(f"   Cada segunda fila: arr[::2, :] =\n{arr[::2, :]}")
    print(f"   Cada segunda columna: arr[:, ::2] =\n{arr[:, ::2]}")
    print(f"   Submatriz con paso: arr[1:4:2, 1:5:2] =\n{arr[1:4:2, 1:5:2]}")
    
    print("\n🎯 4. Indexado booleano:")
    mascara = arr > 10
    print(f"   Máscara (arr > 10):\n{mascara}")
    elementos_mayores = arr[mascara]
    print(f"   Elementos > 10: {elementos_mayores}")
    
    # Condiciones múltiples
    mascara_compleja = (arr > 5) & (arr < 15)
    print(f"   Elementos entre 5 y 15: {arr[mascara_compleja]}")
    
    print("\n🎯 5. Indexado con arrays:")
    filas = np.array([0, 2, 3])
    columnas = np.array([1, 3, 4])
    print(f"   Filas seleccionadas {filas}: arr[filas, :] =\n{arr[filas, :]}")
    print(f"   Elementos específicos arr[filas, columnas] = {arr[filas, columnas]}")
    
    print("\n🎯 6. Modificación con indexado:")
    arr_copia = arr.copy()
    arr_copia[arr_copia > 15] = 999  # Cambiar elementos > 15 a 999
    print(f"   Array modificado (>15 → 999):\n{arr_copia}")
    
    print("\n✅ Sección 3 completada - ¡Indexado dominado!")


def seccion_4_operaciones_matematicas():
    """
    SECCIÓN 4: Operaciones Matemáticas
    - Operaciones elemento a elemento
    - Funciones matemáticas universales
    - Operaciones de reducción
    - Broadcasting
    """
    print("\n📚 SECCIÓN 4: OPERACIONES MATEMÁTICAS")
    print("=" * 50)
    
    # Arrays de ejemplo
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[7, 8, 9], [10, 11, 12]])
    
    print(f"Array A:\n{a}")
    print(f"Array B:\n{b}")
    
    print("\n➕ 1. Operaciones aritméticas básicas:")
    print(f"   A + B =\n{a + b}")
    print(f"   A - B =\n{a - b}")
    print(f"   A * B (elemento a elemento) =\n{a * b}")
    print(f"   A / B =\n{a / b}")
    print(f"   A ** 2 =\n{a ** 2}")
    
    print("\n🔢 2. Funciones matemáticas universales:")
    x = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
    print(f"   x = {x}")
    print(f"   sin(x) = {np.sin(x)}")
    print(f"   cos(x) = {np.cos(x)}")
    print(f"   exp(x) = {np.exp(x)}")
    print(f"   log(x+1) = {np.log(x + 1)}")
    print(f"   sqrt(x+1) = {np.sqrt(x + 1)}")
    
    print("\n📊 3. Operaciones de reducción:")
    matriz = np.random.randint(1, 10, (3, 4))
    print(f"   Matriz aleatoria:\n{matriz}")
    print(f"   Suma total: {np.sum(matriz)}")
    print(f"   Suma por filas: {np.sum(matriz, axis=1)}")
    print(f"   Suma por columnas: {np.sum(matriz, axis=0)}")
    print(f"   Media: {np.mean(matriz):.2f}")
    print(f"   Mediana: {np.median(matriz):.2f}")
    print(f"   Desviación estándar: {np.std(matriz):.2f}")
    print(f"   Mínimo: {np.min(matriz)}, Máximo: {np.max(matriz)}")
    
    print("\n📡 4. Broadcasting - ¡La magia de NumPy!")
    print("   Broadcasting permite operaciones entre arrays de diferentes formas")
    
    # Ejemplo 1: Array 2D + escalar
    matriz_2d = np.array([[1, 2, 3], [4, 5, 6]])
    escalar = 10
    resultado1 = matriz_2d + escalar
    print(f"   Matriz 2D + escalar:\n{matriz_2d} + {escalar} =\n{resultado1}")
    
    # Ejemplo 2: Array 2D + Array 1D
    vector = np.array([10, 20, 30])
    resultado2 = matriz_2d + vector
    print(f"   Matriz 2D + vector:\n{matriz_2d} +\n{vector} =\n{resultado2}")
    
    # Ejemplo 3: Broadcasting con diferentes dimensiones
    col_vector = np.array([[100], [200]])
    resultado3 = matriz_2d + col_vector
    print(f"   Matriz 2D + vector columna:\n{matriz_2d} +\n{col_vector} =\n{resultado3}")
    
    print("\n🧮 5. Álgebra lineal:")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print(f"   Matriz A:\n{A}")
    print(f"   Matriz B:\n{B}")
    print(f"   Producto matricial A @ B =\n{A @ B}")
    print(f"   Determinante de A: {np.linalg.det(A):.2f}")
    print(f"   Traza de A: {np.trace(A)}")
    
    # Resolver sistema de ecuaciones Ax = b
    b = np.array([1, 2])
    x = np.linalg.solve(A, b)
    print(f"   Solución Ax = b, donde b = {b}: x = {x}")
    
    print("\n✅ Sección 4 completada - ¡Matemáticas poderosas!")


def seccion_5_manipulacion_forma():
    """
    SECCIÓN 5: Manipulación de Forma y Dimensiones
    - Reshape, flatten, ravel
    - Transpose
    - Concatenación y división
    - Apilado de arrays
    """
    print("\n📚 SECCIÓN 5: MANIPULACIÓN DE FORMA Y DIMENSIONES")
    print("=" * 50)
    
    # Array de ejemplo
    arr_original = np.arange(12)
    print(f"Array original: {arr_original} (forma: {arr_original.shape})")
    
    print("\n🔄 1. Cambio de forma (reshape):")
    arr_2d = arr_original.reshape(3, 4)
    arr_3d = arr_original.reshape(2, 2, 3)
    
    print(f"   Reshape a (3,4):\n{arr_2d}")
    print(f"   Reshape a (2,2,3):\n{arr_3d}")
    
    # Reshape automático
    arr_auto = arr_original.reshape(3, -1)  # -1 calcula automáticamente
    print(f"   Reshape automático (3,-1):\n{arr_auto}")
    
    print("\n📏 2. Aplanar arrays:")
    print(f"   flatten(): {arr_2d.flatten()}")
    print(f"   ravel(): {arr_2d.ravel()}")
    print(f"   reshape(-1): {arr_2d.reshape(-1)}")
    
    print("\n🔄 3. Transposición:")
    matriz = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"   Matriz original (2x3):\n{matriz}")
    print(f"   Transpuesta .T (3x2):\n{matriz.T}")
    print(f"   Transpuesta con transpose():\n{np.transpose(matriz)}")
    
    print("\n🔗 4. Concatenación de arrays:")
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    
    print(f"   Array A:\n{a}")
    print(f"   Array B:\n{b}")
    
    # Concatenación vertical y horizontal
    concat_v = np.concatenate([a, b], axis=0)  # Vertical
    concat_h = np.concatenate([a, b], axis=1)  # Horizontal
    
    print(f"   Concatenación vertical (axis=0):\n{concat_v}")
    print(f"   Concatenación horizontal (axis=1):\n{concat_h}")
    
    # Funciones específicas
    vstack_result = np.vstack([a, b])  # Vertical stack
    hstack_result = np.hstack([a, b])  # Horizontal stack
    
    print(f"   vstack():\n{vstack_result}")
    print(f"   hstack():\n{hstack_result}")
    
    print("\n📚 5. Apilado de arrays:")
    # Crear un nuevo eje
    stack_axis0 = np.stack([a, b], axis=0)  # Nueva primera dimensión
    stack_axis2 = np.stack([a, b], axis=2)  # Nueva tercera dimensión
    
    print(f"   stack(axis=0) - forma {stack_axis0.shape}:\n{stack_axis0}")
    print(f"   stack(axis=2) - forma {stack_axis2.shape}:\n{stack_axis2}")
    
    print("\n✂️ 6. División de arrays:")
    arr_grande = np.arange(12).reshape(4, 3)
    print(f"   Array grande (4x3):\n{arr_grande}")
    
    # Dividir en partes iguales
    dividido_v = np.split(arr_grande, 2, axis=0)  # 2 partes verticalmente
    dividido_h = np.split(arr_grande, 3, axis=1)  # 3 partes horizontalmente
    
    print(f"   Dividido verticalmente (2 partes):")
    for i, parte in enumerate(dividido_v):
        print(f"     Parte {i+1}:\n{parte}")
    
    print(f"   Dividido horizontalmente (3 partes):")
    for i, parte in enumerate(dividido_h):
        print(f"     Parte {i+1}:\n{parte}")
    
    print("\n✅ Sección 5 completada - ¡Formas dominadas!")


def seccion_6_arrays_avanzados():
    """
    SECCIÓN 6: Técnicas Avanzadas
    - Vectorización
    - Funciones personalizadas (ufunc)
    - Where, select, choose
    - Unique, sorting
    """
    print("\n📚 SECCIÓN 6: TÉCNICAS AVANZADAS")
    print("=" * 50)
    
    print("⚡ 1. Vectorización - Evitar bucles for:")
    
    # Ejemplo: calcular distancias euclidianas
    puntos_x = np.array([1, 2, 3, 4, 5])
    puntos_y = np.array([2, 4, 1, 3, 5])
    origen_x, origen_y = 0, 0
    
    # Forma pythónica (lenta)
    inicio = time.time()
    distancias_python = []
    for x, y in zip(puntos_x, puntos_y):
        dist = ((x - origen_x)**2 + (y - origen_y)**2)**0.5
        distancias_python.append(dist)
    tiempo_python = time.time() - inicio
    
    # Forma vectorizada (rápida)
    inicio = time.time()
    distancias_numpy = np.sqrt((puntos_x - origen_x)**2 + (puntos_y - origen_y)**2)
    tiempo_numpy = time.time() - inicio
    
    print(f"   Puntos: ({puntos_x}, {puntos_y})")
    print(f"   Distancias (Python): {distancias_python}")
    print(f"   Distancias (NumPy): {distancias_numpy}")
    print(f"   ⚡ Vectorización: {tiempo_python/tiempo_numpy:.1f}x más rápida")
    
    print("\n🔧 2. Función where - Selección condicional:")
    datos = np.array([-2, -1, 0, 1, 2, 3, 4, 5])
    
    # Reemplazar negativos con 0
    resultado_where = np.where(datos < 0, 0, datos)
    print(f"   Datos originales: {datos}")
    print(f"   Negativos → 0: {resultado_where}")
    
    # Condición múltiple
    resultado_complejo = np.where(datos < 0, 'negativo', 
                                 np.where(datos == 0, 'cero', 'positivo'))
    print(f"   Clasificación: {resultado_complejo}")
    
    print("\n🎯 3. Función select - Múltiples condiciones:")
    valores = np.array([85, 92, 78, 96, 65, 88, 73, 91])
    condiciones = [
        valores >= 90,  # Excelente
        valores >= 80,  # Bueno
        valores >= 70,  # Regular
    ]
    opciones = ['Excelente', 'Bueno', 'Regular']
    calificaciones = np.select(condiciones, opciones, default='Insuficiente')
    
    print(f"   Puntajes: {valores}")
    print(f"   Calificaciones: {calificaciones}")
    
    print("\n🔍 4. Valores únicos y ordenamiento:")
    datos_desordenados = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    
    # Valores únicos
    unicos = np.unique(datos_desordenados)
    unicos_counts = np.unique(datos_desordenados, return_counts=True)
    
    print(f"   Datos: {datos_desordenados}")
    print(f"   Únicos: {unicos}")
    print(f"   Únicos con conteos: {dict(zip(unicos_counts[0], unicos_counts[1]))}")
    
    # Ordenamiento
    ordenado = np.sort(datos_desordenados)
    indices_orden = np.argsort(datos_desordenados)
    
    print(f"   Ordenado: {ordenado}")
    print(f"   Índices de ordenamiento: {indices_orden}")
    
    # Ordenamiento por columnas en matriz
    matriz = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
    print(f"   Matriz original:\n{matriz}")
    print(f"   Ordenada por filas:\n{np.sort(matriz, axis=1)}")
    print(f"   Ordenada por columnas:\n{np.sort(matriz, axis=0)}")
    
    print("\n🧮 5. Funciones de agregación avanzadas:")
    datos_2d = np.random.randint(1, 100, (4, 5))
    print(f"   Matriz aleatoria (4x5):\n{datos_2d}")
    
    print(f"   Percentiles [25, 50, 75]: {np.percentile(datos_2d, [25, 50, 75])}")
    print(f"   Valor más frecuente por fila:")
    for i, fila in enumerate(datos_2d):
        valores, counts = np.unique(fila, return_counts=True)
        moda = valores[np.argmax(counts)]
        print(f"     Fila {i}: {moda}")
    
    print("\n✅ Sección 6 completada - ¡Técnicas avanzadas dominadas!")


def seccion_7_aplicaciones_practicas():
    """
    SECCIÓN 7: Aplicaciones Prácticas
    - Procesamiento de imágenes
    - Análisis de datos científicos
    - Simulaciones Monte Carlo
    - Procesamiento de señales
    """
    print("\n📚 SECCIÓN 7: APLICACIONES PRÁCTICAS")
    print("=" * 50)
    
    print("🖼️ 1. Simulación de procesamiento de imágenes:")
    # Crear una "imagen" sintética (matriz de píxeles)
    altura, ancho = 50, 50
    imagen = np.random.randint(0, 256, (altura, ancho, 3), dtype=np.uint8)
    
    print(f"   Imagen sintética: {imagen.shape} (altura x ancho x canales RGB)")
    print(f"   Valor promedio por canal: R={np.mean(imagen[:,:,0]):.1f}, "
          f"G={np.mean(imagen[:,:,1]):.1f}, B={np.mean(imagen[:,:,2]):.1f}")
    
    # Conversión a escala de grises
    gris = np.mean(imagen, axis=2).astype(np.uint8)
    print(f"   Imagen en gris: {gris.shape}, promedio: {np.mean(gris):.1f}")
    
    # Aplicar filtro (blur simple)
    kernel = np.ones((3, 3)) / 9  # Kernel de promedio 3x3
    print(f"   Kernel de blur aplicado: {kernel.shape}")
    
    print("\n📊 2. Análisis estadístico de datos científicos:")
    # Simular datos de temperatura diaria por un año
    np.random.seed(42)
    dias = np.arange(365)
    temperatura_base = 20 + 10 * np.sin(2 * np.pi * dias / 365)  # Ciclo anual
    ruido = np.random.normal(0, 3, 365)  # Variabilidad diaria
    temperaturas = temperatura_base + ruido
    
    print(f"   Datos de temperatura: {len(temperaturas)} días")
    print(f"   Estadísticas:")
    print(f"     Promedio anual: {np.mean(temperaturas):.1f}°C")
    print(f"     Máxima: {np.max(temperaturas):.1f}°C (día {np.argmax(temperaturas)+1})")
    print(f"     Mínima: {np.min(temperaturas):.1f}°C (día {np.argmin(temperaturas)+1})")
    print(f"     Desviación estándar: {np.std(temperaturas):.1f}°C")
    
    # Análisis por estaciones
    invierno = temperaturas[:90]
    primavera = temperaturas[90:180]
    verano = temperaturas[180:270]
    otono = temperaturas[270:]
    
    print(f"   Promedios estacionales:")
    print(f"     Invierno: {np.mean(invierno):.1f}°C")
    print(f"     Primavera: {np.mean(primavera):.1f}°C")
    print(f"     Verano: {np.mean(verano):.1f}°C")
    print(f"     Otoño: {np.mean(otono):.1f}°C")
    
    print("\n🎲 3. Simulación Monte Carlo - Estimación de π:")
    n_puntos = 100000
    # Generar puntos aleatorios en el cuadrado [-1,1] x [-1,1]
    x = np.random.uniform(-1, 1, n_puntos)
    y = np.random.uniform(-1, 1, n_puntos)
    
    # Verificar cuáles están dentro del círculo unitario
    dentro_circulo = (x**2 + y**2) <= 1
    puntos_dentro = np.sum(dentro_circulo)
    
    # Estimar π
    pi_estimado = 4 * puntos_dentro / n_puntos
    error = abs(pi_estimado - np.pi)
    
    print(f"   Puntos generados: {n_puntos:,}")
    print(f"   Puntos dentro del círculo: {puntos_dentro:,}")
    print(f"   π estimado: {pi_estimado:.6f}")
    print(f"   π real: {np.pi:.6f}")
    print(f"   Error: {error:.6f} ({error/np.pi*100:.4f}%)")
    
    print("\n📡 4. Procesamiento de señales:")
    # Generar señal sintética
    t = np.linspace(0, 2, 1000)  # 2 segundos, 1000 puntos
    frecuencia1, frecuencia2 = 5, 20  # Hz
    señal = (np.sin(2*np.pi*frecuencia1*t) + 
             0.5*np.sin(2*np.pi*frecuencia2*t) + 
             0.1*np.random.normal(0, 1, len(t)))
    
    print(f"   Señal generada: {len(señal)} muestras en {t[-1]} segundos")
    print(f"   Componentes: {frecuencia1}Hz + {frecuencia2}Hz + ruido")
    
    # Análisis estadístico de la señal
    print(f"   Estadísticas de la señal:")
    print(f"     Amplitud promedio: {np.mean(np.abs(señal)):.3f}")
    print(f"     RMS: {np.sqrt(np.mean(señal**2)):.3f}")
    print(f"     Pico máximo: {np.max(np.abs(señal)):.3f}")
    
    # Detección de picos simples
    umbral = 1.5
    picos = np.where(np.abs(señal) > umbral)[0]
    print(f"     Picos detectados (|amplitud| > {umbral}): {len(picos)}")
    
    print("\n🧬 5. Análisis de datos biológicos (simulado):")
    # Simular datos de expresión génica
    n_genes = 1000
    n_muestras = 50
    expresion_genes = np.random.lognormal(0, 1, (n_genes, n_muestras))
    
    print(f"   Datos de expresión: {n_genes} genes x {n_muestras} muestras")
    
    # Encontrar genes altamente expresados
    expresion_promedio = np.mean(expresion_genes, axis=1)
    genes_altos = np.where(expresion_promedio > np.percentile(expresion_promedio, 95))[0]
    
    print(f"   Genes altamente expresados (>95 percentil): {len(genes_altos)}")
    print(f"   Expresión promedio más alta: {np.max(expresion_promedio):.2f}")
    
    # Correlación entre muestras
    correlaciones = np.corrcoef(expresion_genes.T)
    correlacion_promedio = np.mean(correlaciones[np.triu_indices(n_muestras, k=1)])
    print(f"   Correlación promedio entre muestras: {correlacion_promedio:.3f}")
    
    print("\n✅ Sección 7 completada - ¡Aplicaciones prácticas dominadas!")


def seccion_8_optimizacion_rendimiento():
    """
    SECCIÓN 8: Optimización y Rendimiento
    - Mejores prácticas de rendimiento
    - Uso eficiente de memoria
    - Vectorización avanzada
    - Comparaciones de velocidad
    """
    print("\n📚 SECCIÓN 8: OPTIMIZACIÓN Y RENDIMIENTO")
    print("=" * 50)
    
    print("⚡ 1. Comparación de métodos de creación:")
    n = 1000000
    
    # Método 1: Lista de Python + conversión
    inicio = time.time()
    lista = list(range(n))
    arr_desde_lista = np.array(lista)
    tiempo_lista = time.time() - inicio
    
    # Método 2: np.arange directo
    inicio = time.time()
    arr_arange = np.arange(n)
    tiempo_arange = time.time() - inicio
    
    # Método 3: np.empty + asignación
    inicio = time.time()
    arr_empty = np.empty(n)
    arr_empty[:] = range(n)
    tiempo_empty = time.time() - inicio
    
    print(f"   Crear array de {n:,} elementos:")
    print(f"     Lista → array: {tiempo_lista:.4f}s")
    print(f"     np.arange: {tiempo_arange:.4f}s ({tiempo_lista/tiempo_arange:.1f}x más rápido)")
    print(f"     np.empty + asignación: {tiempo_empty:.4f}s")
    
    print("\n💾 2. Gestión eficiente de memoria:")
    
    # Tipos de datos y memoria
    arr_int64 = np.arange(1000, dtype=np.int64)
    arr_int32 = np.arange(1000, dtype=np.int32)
    arr_int8 = np.arange(1000, dtype=np.int8)
    
    print(f"   Memoria por tipo de dato (1000 elementos):")
    print(f"     int64: {arr_int64.nbytes:,} bytes")
    print(f"     int32: {arr_int32.nbytes:,} bytes ({arr_int64.nbytes//arr_int32.nbytes}x menos)")
    print(f"     int8: {arr_int8.nbytes:,} bytes ({arr_int64.nbytes//arr_int8.nbytes}x menos)")
    
    # Views vs copias
    arr_original = np.arange(100000)
    
    inicio = time.time()
    view = arr_original[::2]  # View (no copia memoria)
    tiempo_view = time.time() - inicio
    
    inicio = time.time()
    copia = arr_original[::2].copy()  # Copia explícita
    tiempo_copia = time.time() - inicio
    
    print(f"\n   Views vs Copias:")
    print(f"     Crear view: {tiempo_view:.6f}s")
    print(f"     Crear copia: {tiempo_copia:.6f}s ({tiempo_copia/tiempo_view:.1f}x más lento)")
    print(f"     Memoria view: comparte con original")
    print(f"     Memoria copia: {copia.nbytes:,} bytes adicionales")
    
    print("\n🔄 3. Vectorización vs bucles:")
    
    # Operación: calcular raíz cuadrada + seno
    datos = np.random.random(100000)
    
    # Bucle Python
    inicio = time.time()
    resultado_bucle = []
    for x in datos:
        resultado_bucle.append(np.sqrt(x) + np.sin(x))
    resultado_bucle = np.array(resultado_bucle)
    tiempo_bucle = time.time() - inicio
    
    # Vectorizado
    inicio = time.time()
    resultado_vectorizado = np.sqrt(datos) + np.sin(datos)
    tiempo_vectorizado = time.time() - inicio
    
    print(f"   Operación: sqrt(x) + sin(x) en {len(datos):,} elementos")
    print(f"     Bucle Python: {tiempo_bucle:.4f}s")
    print(f"     Vectorizado: {tiempo_vectorizado:.4f}s")
    print(f"     🚀 Mejora: {tiempo_bucle/tiempo_vectorizado:.1f}x más rápido")
    print(f"     Resultados idénticos: {np.allclose(resultado_bucle, resultado_vectorizado)}")
    
    print("\n🧮 4. Operaciones in-place vs nuevos arrays:")
    
    arr_test = np.random.random(100000)
    
    # Operación que crea nuevo array
    inicio = time.time()
    resultado_nuevo = arr_test * 2 + 1
    tiempo_nuevo = time.time() - inicio
    
    # Operación in-place
    arr_inplace = arr_test.copy()
    inicio = time.time()
    arr_inplace *= 2
    arr_inplace += 1
    tiempo_inplace = time.time() - inicio
    
    print(f"   Operación: x = x * 2 + 1 en {len(arr_test):,} elementos")
    print(f"     Nuevo array: {tiempo_nuevo:.6f}s")
    print(f"     In-place: {tiempo_inplace:.6f}s ({tiempo_nuevo/tiempo_inplace:.1f}x más rápido)")
    print(f"     Memoria ahorrada: {resultado_nuevo.nbytes:,} bytes")
    
    print("\n🎯 5. Consejos de optimización:")
    consejos = [
        "• Usa el tipo de dato más pequeño posible (int32 vs int64)",
        "• Prefiere operaciones vectorizadas sobre bucles",
        "• Usa views en lugar de copias cuando sea posible",
        "• Aprovecha operaciones in-place para ahorrar memoria",
        "• Pre-aloca arrays con np.empty() si conoces el tamaño",
        "• Usa np.einsum() para operaciones tensoriales complejas",
        "• Considera numba o Cython para bucles inevitables",
        "• Perfila tu código con %timeit en Jupyter"
    ]
    
    for consejo in consejos:
        print(f"   {consejo}")
    
    print("\n✅ Sección 8 completada - ¡Rendimiento optimizado!")


def mostrar_resumen_numpy():
    """
    Resumen completo de funciones NumPy más importantes
    """
    print("\n📋 RESUMEN DE FUNCIONES NUMPY MÁS IMPORTANTES")
    print("=" * 60)
    
    categorias = {
        "🏗️ CREACIÓN DE ARRAYS": [
            "np.array(lista) - Crear desde lista",
            "np.zeros(forma) - Array de ceros",
            "np.ones(forma) - Array de unos", 
            "np.eye(n) - Matriz identidad",
            "np.arange(inicio, fin, paso) - Secuencia",
            "np.linspace(inicio, fin, num) - Puntos equiespaciados",
            "np.random.random(forma) - Números aleatorios [0,1)",
            "np.random.normal(μ, σ, forma) - Distribución normal"
        ],
        
        "🎯 INDEXADO Y SELECCIÓN": [
            "arr[i, j] - Elemento específico",
            "arr[inicio:fin] - Slicing",
            "arr[arr > valor] - Indexado booleano",
            "np.where(condición, x, y) - Selección condicional"
        ],
        
        "🔢 OPERACIONES MATEMÁTICAS": [
            "np.sum(), np.mean(), np.std() - Estadísticas",
            "np.min(), np.max(), np.argmin(), np.argmax() - Extremos",
            "np.sin(), np.cos(), np.exp(), np.log() - Funciones matemáticas",
            "np.sqrt(), np.abs(), np.round() - Operaciones básicas"
        ],
        
        "🔄 MANIPULACIÓN DE FORMA": [
            "arr.reshape(nueva_forma) - Cambiar forma",
            "arr.flatten() - Aplanar a 1D",
            "arr.T - Transpuesta",
            "np.concatenate([a, b], axis) - Concatenar",
            "np.stack([a, b], axis) - Apilar"
        ],
        
        "🧮 ÁLGEBRA LINEAL": [
            "A @ B - Producto matricial",
            "np.linalg.det(A) - Determinante",
            "np.linalg.inv(A) - Inversa",
            "np.linalg.solve(A, b) - Resolver Ax = b"
        ]
    }
    
    for categoria, funciones in categorias.items():
        print(f"\n{categoria}:")
        for funcion in funciones:
            print(f"   {funcion}")
    
    print(f"\n🌐 RECURSOS ADICIONALES:")
    print(f"   • Documentación oficial: https://numpy.org/doc/")
    print(f"   • Tutorial interactivo: https://numpy.org/learn/")
    print(f"   • Cheat sheet: https://numpy.org/doc/stable/user/quickstart.html")
    print("=" * 60)


def menu_interactivo_numpy():
    """
    Menú interactivo para navegar por las secciones
    """
    secciones = {
        '1': ('Introducción a NumPy', seccion_1_introduccion),
        '2': ('Creación de Arrays', seccion_2_creacion_arrays),
        '3': ('Indexado y Slicing', seccion_3_indexado_slicing),
        '4': ('Operaciones Matemáticas', seccion_4_operaciones_matematicas),
        '5': ('Manipulación de Forma', seccion_5_manipulacion_forma),
        '6': ('Técnicas Avanzadas', seccion_6_arrays_avanzados),
        '7': ('Aplicaciones Prácticas', seccion_7_aplicaciones_practicas),
        '8': ('Optimización y Rendimiento', seccion_8_optimizacion_rendimiento),
        'todo': ('Ejecutar todo el tutorial', lambda: ejecutar_tutorial_completo()),
        'resumen': ('Mostrar resumen de funciones', mostrar_resumen_numpy)
    }
    
    print("\n🔢 TUTORIAL INTERACTIVO DE NUMPY")
    print("=" * 50)
    print("Selecciona la sección que quieres explorar:")
    
    for key, (descripcion, _) in secciones.items():
        print(f"   {key}) {descripcion}")
    
    print("   0) Salir")
    
    while True:
        try:
            opcion = input("\n👉 Ingresa tu opción: ").strip().lower()
            
            if opcion == '0':
                print("¡Gracias por explorar NumPy! 🔢 ¡Ahora eres un ninja de los arrays!")
                break
            elif opcion in secciones:
                print(f"\n🚀 Ejecutando: {secciones[opcion][0]}")
                print("-" * 50)
                secciones[opcion][1]()
                input("\n⏸️ Presiona Enter para continuar...")
            else:
                print("❌ Opción no válida. Por favor, intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n🛑 Tutorial terminado por el usuario. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            print("💡 Continuando con el tutorial...")


def ejecutar_tutorial_completo():
    """
    Ejecuta todas las secciones en orden
    """
    print("🚀 EJECUTANDO TUTORIAL COMPLETO DE NUMPY")
    print("=" * 60)
    
    secciones = [
        seccion_1_introduccion,
        seccion_2_creacion_arrays,
        seccion_3_indexado_slicing,
        seccion_4_operaciones_matematicas,
        seccion_5_manipulacion_forma,
        seccion_6_arrays_avanzados,
        seccion_7_aplicaciones_practicas,
        seccion_8_optimizacion_rendimiento
    ]
    
    for i, seccion in enumerate(secciones, 1):
        print(f"\n🎯 Ejecutando sección {i}/{len(secciones)}")
        try:
            seccion()
            if i < len(secciones):
                continuar = input("\n⏸️ Presiona Enter para continuar (o 'q' para salir): ")
                if continuar.lower() == 'q':
                    break
        except Exception as e:
            print(f"❌ Error en sección {i}: {e}")
            continuar = input("¿Continuar con la siguiente sección? (s/n): ")
            if continuar.lower() != 's':
                break
    
    print("\n🎉 ¡Tutorial completo de NumPy finalizado!")
    mostrar_resumen_numpy()


# Verificar instalación de NumPy
if __name__ == "__main__":
    try:
        import numpy as np
        print("✅ NumPy está correctamente instalado")
        print(f"📦 Versión de NumPy: {np.__version__}")
        
        # Mostrar información del sistema
        print(f"🖥️ Configuración NumPy:")
        print(f"   • Compilado con BLAS: {np.__config__.show() is None}")
        print(f"   • Soporte para arrays grandes: {np.can_cast(np.int64, np.intp)}")
        
        # Mostrar resumen primero
        mostrar_resumen_numpy()
        
        # Iniciar menú interactivo
        menu_interactivo_numpy()
        
    except ImportError as e:
        print("❌ Error: NumPy no está instalado")
        print("💡 Instala NumPy con: pip install numpy")
        print(f"   Detalles del error: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        print("💡 Verifica tu instalación de NumPy")