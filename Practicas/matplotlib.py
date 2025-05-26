# TUTORIAL COMPLETO DE MATPLOTLIB
# Visualización de datos con Python
# Autor: David
# Fecha: Mayo 2025

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import math

# Configuración global para mejorar la apariencia de los gráficos
plt.style.use('seaborn-v0_8')  # Estilo moderno y limpio
plt.rcParams['figure.figsize'] = (10, 6)  # Tamaño por defecto
plt.rcParams['font.size'] = 12


def ejemplo_1_grafico_lineal_basico():
    """
    EJEMPLO 1: Gráfico de líneas básico
    - Función matemática simple
    - Personalización básica de colores y etiquetas
    """
    print("📊 EJEMPLO 1: Gráfico de líneas básico")
    print("-" * 50)
    
    # Datos de ejemplo: función seno
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)
    
    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='blue', linewidth=2, label='sen(x)')
    
    # Personalización
    plt.title('Función Seno', fontsize=16, fontweight='bold')
    plt.xlabel('x (radianes)', fontsize=12)
    plt.ylabel('sen(x)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()
    
    print("✅ Gráfico de líneas básico completado\n")


def ejemplo_2_multiples_funciones():
    """
    EJEMPLO 2: Múltiples funciones en un mismo gráfico
    - Varias series de datos
    - Diferentes estilos de línea
    - Leyenda personalizada
    """
    print("📊 EJEMPLO 2: Múltiples funciones")
    print("-" * 50)
    
    # Datos
    x = np.linspace(0, 2*np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x/2)
    
    # Crear el gráfico
    plt.figure(figsize=(12, 7))
    
    # Múltiples líneas con diferentes estilos
    plt.plot(x, y1, 'b-', linewidth=2, label='sen(x)')
    plt.plot(x, y2, 'r--', linewidth=2, label='cos(x)')
    plt.plot(x, y3, 'g:', linewidth=2, label='tan(x/2)')
    
    # Personalización avanzada
    plt.title('Funciones Trigonométricas', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('x (radianes)', fontsize=14)
    plt.ylabel('f(x)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper right', fontsize=12)
    
    # Limitar el eje Y para mejor visualización
    plt.ylim(-2, 2)
    
    plt.tight_layout()
    plt.show()
    
    print("✅ Gráfico de múltiples funciones completado\n")


def ejemplo_3_grafico_barras():
    """
    EJEMPLO 3: Gráfico de barras
    - Datos categóricos
    - Personalización de colores
    - Anotaciones en barras
    """
    print("📊 EJEMPLO 3: Gráfico de barras")
    print("-" * 50)
    
    # Datos de ejemplo: ventas por mes
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
    ventas = [1200, 1350, 1100, 1400, 1600, 1800]
    colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3']
    
    # Crear el gráfico
    plt.figure(figsize=(10, 7))
    barras = plt.bar(meses, ventas, color=colores, alpha=0.8, edgecolor='black', linewidth=1)
    
    # Agregar valores en las barras
    for barra, valor in zip(barras, ventas):
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., altura + 20,
                f'${valor:,}', ha='center', va='bottom', fontweight='bold')
    
    # Personalización
    plt.title('Ventas Mensuales 2024', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Mes', fontsize=12)
    plt.ylabel('Ventas ($)', fontsize=12)
    plt.grid(True, axis='y', alpha=0.3)
    
    # Formatear eje Y
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    plt.tight_layout()
    plt.show()
    
    print("✅ Gráfico de barras completado\n")


def ejemplo_4_histograma():
    """
    EJEMPLO 4: Histograma
    - Distribución de datos
    - Análisis estadístico visual
    - Curva de densidad
    """
    print("📊 EJEMPLO 4: Histograma con análisis estadístico")
    print("-" * 50)
    
    # Generar datos aleatorios (distribución normal)
    np.random.seed(42)
    datos = np.random.normal(100, 15, 1000)  # Media=100, Desv=15, n=1000
    
    # Crear el histograma
    plt.figure(figsize=(12, 7))
    
    # Histograma
    n, bins, patches = plt.hist(datos, bins=30, density=True, alpha=0.7, 
                               color='skyblue', edgecolor='black', linewidth=0.5)
    
    # Curva de densidad teórica
    x_curva = np.linspace(datos.min(), datos.max(), 100)
    y_curva = (1/np.sqrt(2*np.pi*15**2)) * np.exp(-0.5*((x_curva-100)/15)**2)
    plt.plot(x_curva, y_curva, 'r-', linewidth=3, label='Distribución Normal Teórica')
    
    # Líneas de referencia
    plt.axvline(np.mean(datos), color='red', linestyle='--', linewidth=2, label=f'Media: {np.mean(datos):.1f}')
    plt.axvline(np.median(datos), color='green', linestyle='--', linewidth=2, label=f'Mediana: {np.median(datos):.1f}')
    
    # Personalización
    plt.title('Distribución de Datos - Análisis Estadístico', fontsize=16, fontweight='bold')
    plt.xlabel('Valores', fontsize=12)
    plt.ylabel('Densidad', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Mostrar estadísticas
    print(f"📈 Estadísticas descriptivas:")
    print(f"   Media: {np.mean(datos):.2f}")
    print(f"   Mediana: {np.median(datos):.2f}")
    print(f"   Desviación estándar: {np.std(datos):.2f}")
    print(f"   Mínimo: {np.min(datos):.2f}")
    print(f"   Máximo: {np.max(datos):.2f}")
    print("✅ Histograma completado\n")


def ejemplo_5_scatter_plot():
    """
    EJEMPLO 5: Gráfico de dispersión (Scatter plot)
    - Relación entre variables
    - Colores según categorías
    - Línea de tendencia
    """
    print("📊 EJEMPLO 5: Gráfico de dispersión con línea de tendencia")
    print("-" * 50)
    
    # Generar datos con correlación
    np.random.seed(42)
    n = 100
    x = np.random.normal(50, 15, n)
    y = 2*x + np.random.normal(0, 20, n)  # Relación lineal con ruido
    colores = np.random.choice(['A', 'B', 'C'], n)
    
    # Crear el scatter plot
    plt.figure(figsize=(12, 8))
    
    # Puntos por categoría
    for categoria in ['A', 'B', 'C']:
        mask = colores == categoria
        plt.scatter(x[mask], y[mask], label=f'Categoría {categoria}', 
                   alpha=0.7, s=60)
    
    # Línea de tendencia
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r--", alpha=0.8, linewidth=2, 
             label=f'Tendencia: y = {z[0]:.2f}x + {z[1]:.2f}')
    
    # Personalización
    plt.title('Relación entre Variables X e Y', fontsize=16, fontweight='bold')
    plt.xlabel('Variable X', fontsize=12)
    plt.ylabel('Variable Y', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Calcular correlación
    correlacion = np.corrcoef(x, y)[0, 1]
    plt.text(0.05, 0.95, f'Correlación: {correlacion:.3f}', 
             transform=plt.gca().transAxes, fontsize=12, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
    
    plt.tight_layout()
    plt.show()
    
    print(f"📈 Coeficiente de correlación: {correlacion:.3f}")
    print("✅ Gráfico de dispersión completado\n")


def ejemplo_6_subplots():
    """
    EJEMPLO 6: Múltiples subgráficos (Subplots)
    - Organización de múltiples gráficos
    - Diferentes tipos en una figura
    - Compartir ejes
    """
    print("📊 EJEMPLO 6: Múltiples subgráficos")
    print("-" * 50)
    
    # Datos
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.exp(-x/5) * np.sin(x)
    
    # Crear figura con subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Subplot 1: Función seno
    ax1.plot(x, y1, 'b-', linewidth=2)
    ax1.set_title('Función Seno', fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.set_ylabel('sen(x)')
    
    # Subplot 2: Función coseno
    ax2.plot(x, y2, 'r-', linewidth=2)
    ax2.set_title('Función Coseno', fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.set_ylabel('cos(x)')
    
    # Subplot 3: Función exponencial amortiguada
    ax3.plot(x, y3, 'g-', linewidth=2)
    ax3.set_title('Seno Amortiguado', fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.set_xlabel('x')
    ax3.set_ylabel('f(x)')
    
    # Subplot 4: Histograma
    datos_hist = np.random.normal(0, 1, 1000)
    ax4.hist(datos_hist, bins=30, alpha=0.7, color='orange', edgecolor='black')
    ax4.set_title('Distribución Normal', fontweight='bold')
    ax4.set_xlabel('Valores')
    ax4.set_ylabel('Frecuencia')
    ax4.grid(True, alpha=0.3)
    
    # Título general
    fig.suptitle('Colección de Gráficos Matemáticos', fontsize=16, fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    print("✅ Múltiples subgráficos completados\n")


def ejemplo_7_grafico_polar():
    """
    EJEMPLO 7: Gráfico polar
    - Coordenadas polares
    - Patrones circulares
    - Rosa de vientos matemática
    """
    print("📊 EJEMPLO 7: Gráfico polar - Rosa matemática")
    print("-" * 50)
    
    # Datos para rosa matemática
    theta = np.linspace(0, 2*np.pi, 1000)
    r = np.sin(5*theta)  # Rosa de 5 pétalos
    
    # Crear gráfico polar
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7), subplot_kw=dict(projection='polar'))
    
    # Rosa matemática
    ax1.plot(theta, r, color='red', linewidth=2)
    ax1.fill(theta, r, alpha=0.3, color='red')
    ax1.set_title('Rosa Matemática (5 pétalos)', pad=20, fontweight='bold')
    
    # Espiral de Arquímedes
    theta2 = np.linspace(0, 6*np.pi, 1000)
    r2 = theta2
    ax2.plot(theta2, r2, color='blue', linewidth=2)
    ax2.set_title('Espiral de Arquímedes', pad=20, fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    print("✅ Gráficos polares completados\n")


def ejemplo_8_mapa_calor():
    """
    EJEMPLO 8: Mapa de calor (Heatmap)
    - Visualización de matrices
    - Mapas de correlación
    - Datos bidimensionales
    """
    print("📊 EJEMPLO 8: Mapa de calor")
    print("-" * 50)
    
    # Generar datos de ejemplo (matriz de correlación)
    np.random.seed(42)
    variables = ['Ventas', 'Marketing', 'Personal', 'Satisfacción', 'Beneficios']
    n = len(variables)
    
    # Crear matriz de correlación simulada
    data = np.random.rand(n, n)
    data = (data + data.T) / 2  # Hacer simétrica
    np.fill_diagonal(data, 1)  # Diagonal = 1
    
    # Crear mapa de calor
    plt.figure(figsize=(10, 8))
    im = plt.imshow(data, cmap='RdYlBu_r', interpolation='nearest', vmin=-1, vmax=1)
    
    # Personalización
    plt.title('Matriz de Correlación - KPIs Empresariales', fontsize=16, fontweight='bold', pad=20)
    
    # Etiquetas de ejes
    plt.xticks(range(n), variables, rotation=45, ha='right')
    plt.yticks(range(n), variables)
    
    # Agregar valores en las celdas
    for i in range(n):
        for j in range(n):
            plt.text(j, i, f'{data[i, j]:.2f}', ha='center', va='center',
                    color='white' if abs(data[i, j]) > 0.5 else 'black', fontweight='bold')
    
    # Barra de colores
    cbar = plt.colorbar(im, shrink=0.8)
    cbar.set_label('Coeficiente de Correlación', rotation=270, labelpad=20)
    
    plt.tight_layout()
    plt.show()
    
    print("✅ Mapa de calor completado\n")


def ejemplo_9_series_temporales():
    """
    EJEMPLO 9: Series temporales
    - Datos con fechas
    - Tendencias temporales
    - Formato de fechas
    """
    print("📊 EJEMPLO 9: Series temporales")
    print("-" * 50)
    
    # Generar datos de serie temporal
    fechas = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')
    
    # Simular datos de temperatura con tendencia y estacionalidad
    dias = np.arange(len(fechas))
    temperatura = (20 + 10*np.sin(2*np.pi*dias/365) + 
                  2*np.sin(2*np.pi*dias/30) + 
                  np.random.normal(0, 2, len(fechas)))
    
    # Crear el gráfico
    plt.figure(figsize=(15, 8))
    plt.plot(fechas, temperatura, linewidth=1, alpha=0.7, color='blue')
    
    # Agregar media móvil
    ventana = 30
    media_movil = pd.Series(temperatura).rolling(window=ventana).mean()
    plt.plot(fechas, media_movil, linewidth=3, color='red', 
             label=f'Media móvil ({ventana} días)')
    
    # Personalización
    plt.title('Temperatura Diaria - Análisis de Tendencias', fontsize=16, fontweight='bold')
    plt.xlabel('Fecha', fontsize=12)
    plt.ylabel('Temperatura (°C)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Rotar etiquetas de fechas
    plt.xticks(rotation=45)
    
    # Resaltar estaciones
    plt.axvspan(fechas[0], fechas[90], alpha=0.1, color='blue', label='Invierno')
    plt.axvspan(fechas[90], fechas[180], alpha=0.1, color='green', label='Primavera')
    plt.axvspan(fechas[180], fechas[270], alpha=0.1, color='orange', label='Verano')
    plt.axvspan(fechas[270], fechas[360], alpha=0.1, color='brown', label='Otoño')
    
    plt.tight_layout()
    plt.show()
    
    print("✅ Serie temporal completada\n")


def ejemplo_10_grafico_3d():
    """
    EJEMPLO 10: Gráfico 3D
    - Superficies tridimensionales
    - Funciones de dos variables
    - Visualización volumétrica
    """
    print("📊 EJEMPLO 10: Gráfico 3D - Superficie")
    print("-" * 50)
    
    # Crear datos 3D
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    # Crear gráfico 3D
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    
    # Superficie
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, 
                          linewidth=0, antialiased=True)
    
    # Curvas de nivel proyectadas
    ax.contour(X, Y, Z, zdir='z', offset=Z.min(), cmap='viridis', alpha=0.5)
    
    # Personalización
    ax.set_title('Superficie 3D: f(x,y) = sin(√(x² + y²))', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    
    # Barra de colores
    fig.colorbar(surf, shrink=0.5, aspect=20)
    
    plt.tight_layout()
    plt.show()
    
    print("✅ Gráfico 3D completado\n")


def mostrar_consejos_matplotlib():
    """
    Consejos y mejores prácticas para matplotlib
    """
    print("💡 CONSEJOS Y MEJORES PRÁCTICAS DE MATPLOTLIB")
    print("=" * 60)
    
    consejos = [
        "1. Usa plt.style.use() para estilos predefinidos elegantes",
        "2. Siempre agrega títulos descriptivos y etiquetas de ejes",
        "3. Usa plt.tight_layout() para evitar superposiciones",
        "4. Los colores tienen significado: rojo=peligro, verde=bueno, azul=neutral",
        "5. Para datos científicos, usa escalas logarítmicas cuando sea apropiado",
        "6. Las leyendas son cruciales en gráficos con múltiples series",
        "7. Los grids mejoran la legibilidad (usa alpha<1 para sutileza)",
        "8. Para presentaciones, usa figsize=(12, 8) o mayor",
        "9. Guarda en vectorial (PDF, SVG) para publicaciones científicas",
        "10. Usa subplots para comparaciones lado a lado"
    ]
    
    for consejo in consejos:
        print(f"   {consejo}")
    
    print("\n📚 RECURSOS ADICIONALES:")
    print("   - Galería oficial: https://matplotlib.org/stable/gallery/")
    print("   - Cheat sheet: https://matplotlib.org/cheatsheets/")
    print("   - Colormaps: https://matplotlib.org/stable/tutorials/colors/colormaps.html")
    print("=" * 60)


def menu_interactivo():
    """
    Menú interactivo para ejecutar ejemplos específicos
    """
    ejemplos = {
        '1': ('Gráfico de líneas básico', ejemplo_1_grafico_lineal_basico),
        '2': ('Múltiples funciones', ejemplo_2_multiples_funciones),
        '3': ('Gráfico de barras', ejemplo_3_grafico_barras),
        '4': ('Histograma estadístico', ejemplo_4_histograma),
        '5': ('Scatter plot con tendencia', ejemplo_5_scatter_plot),
        '6': ('Múltiples subgráficos', ejemplo_6_subplots),
        '7': ('Gráficos polares', ejemplo_7_grafico_polar),
        '8': ('Mapa de calor', ejemplo_8_mapa_calor),
        '9': ('Series temporales', ejemplo_9_series_temporales),
        '10': ('Gráfico 3D', ejemplo_10_grafico_3d),
        'todo': ('Ejecutar todos los ejemplos', lambda: ejecutar_todos_ejemplos()),
        'consejos': ('Mostrar consejos', mostrar_consejos_matplotlib)
    }
    
    print("\n🎨 TUTORIAL INTERACTIVO DE MATPLOTLIB")
    print("=" * 50)
    print("Selecciona el ejemplo que quieres ver:")
    
    for key, (descripcion, _) in ejemplos.items():
        print(f"   {key}) {descripcion}")
    
    print("   0) Salir")
    
    while True:
        try:
            opcion = input("\n👉 Ingresa tu opción: ").strip().lower()
            
            if opcion == '0':
                print("¡Gracias por usar el tutorial de matplotlib! 🎨")
                break
            elif opcion in ejemplos:
                print(f"\n🚀 Ejecutando: {ejemplos[opcion][0]}")
                ejemplos[opcion][1]()
                input("Presiona Enter para continuar...")
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n🛑 Tutorial terminado por el usuario.")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


def ejecutar_todos_ejemplos():
    """
    Ejecuta todos los ejemplos en secuencia
    """
    print("🚀 EJECUTANDO TODOS LOS EJEMPLOS")
    print("=" * 50)
    
    ejemplos = [
        ejemplo_1_grafico_lineal_basico,
        ejemplo_2_multiples_funciones,
        ejemplo_3_grafico_barras,
        ejemplo_4_histograma,
        ejemplo_5_scatter_plot,
        ejemplo_6_subplots,
        ejemplo_7_grafico_polar,
        ejemplo_8_mapa_calor,
        ejemplo_9_series_temporales,
        ejemplo_10_grafico_3d
    ]
    
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"\n🎯 Ejecutando ejemplo {i}/{len(ejemplos)}")
        try:
            ejemplo()
            if i < len(ejemplos):  # No pausar en el último
                input("Presiona Enter para continuar al siguiente ejemplo...")
        except Exception as e:
            print(f"❌ Error en ejemplo {i}: {e}")
            continuar = input("¿Continuar con el siguiente ejemplo? (s/n): ")
            if continuar.lower() != 's':
                break
    
    print("\n🎉 ¡Todos los ejemplos completados!")


if __name__ == "__main__":
    print("🎨 BIENVENIDO AL TUTORIAL COMPLETO DE MATPLOTLIB")
    print("Visualización de datos profesional con Python")
    print("=" * 60)
    
    try:
        # Verificar que matplotlib esté instalado
        import matplotlib.pyplot as plt
        print("✅ Matplotlib está correctamente instalado")
        
        # Mostrar consejos primero
        mostrar_consejos_matplotlib()
        
        # Iniciar menú interactivo
        menu_interactivo()
        
    except ImportError as e:
        print("❌ Error: matplotlib no está instalado")
        print("💡 Instala matplotlib con: pip install matplotlib")
        print(f"   Detalles del error: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        print("💡 Asegúrate de tener todas las dependencias instaladas:")