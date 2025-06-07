import numpy as np
import matplotlib.pyplot as plt

def funcion_ingenieria_civil(x, alpha=0.1):
    """f(x) = e^(-αx)"""
    return np.exp(-alpha * x)

def funcion_ingenieria_geografica(x, mu=0, sigma=10):
    """f(x) = e^(-(x-μ)²/(2σ²))"""
    return np.exp(-((x - mu)**2) / (2 * sigma**2))

def funcion_ingenieria_industrial(x, k=0.1):
    """f(x) = e^(-kx)"""
    return np.exp(-k * x)

def funcion_ingenieria_electromecanica(x, zeta=0.2, omega_d=1, b=40):
    """f(x) = (1-e^(-ζx)cos(ωₐx))/(2(1-e^(-ζx)cos(ωₐb)))"""
    numerador = 1 - np.exp(-zeta * x) * np.cos(omega_d * x)
    denominador = 2 * (1 - np.exp(-zeta * x) * np.cos(omega_d * b))
    return numerador / denominador

def funcion_ingenieria_electronica(x, omega_0=1):
    """f(x) = 1/√(1+(x/ω₀)²)"""
    return 1 / np.sqrt(1 + (x / omega_0)**2)

def funcion_ingenieria_mecatronica(x):
    """f(x) = (sin(x) + 0.5*cos(2x) + 1.5)/3"""
    return (np.sin(x) + 0.5 * np.cos(2*x) + 1.5) / 3

def funcion_ingenieria_mecanica(x, k=1, x0=5):
    """f(x) = 1/(1+e^(-k(x-x₀)))"""
    return 1 / (1 + np.exp(-k * (x - x0)))

def seleccionar_funcion():
    """Permite al usuario seleccionar la función según su carrera"""
    print("Seleccione su carrera:")
    print("1. Ingeniería Civil")
    print("2. Ingeniería Geográfica Ambiental") 
    print("3. Ingeniería Industrial")
    print("4. Ingeniería Electromecánica")
    print("5. Ingeniería Electrónica")
    print("6. Ingeniería Mecatrónica")
    print("7. Ingeniería Mecánica")
    
    while True:
        try:
            opcion = int(input("\nIngrese el número de su carrera (1-7): "))
            if 1 <= opcion <= 7:
                break
            else:
                print("Por favor ingrese un número entre 1 y 7")
        except ValueError:
            print("Por favor ingrese un número válido")
    
    funciones = {
        1: (funcion_ingenieria_civil, [0, 50], "Ingeniería Civil", "f(x) = e^(-0.1x)"),
        2: (funcion_ingenieria_geografica, [-30, 30], "Ingeniería Geográfica Ambiental", "f(x) = e^(-(x-0)²/(2·10²))"),
        3: (funcion_ingenieria_industrial, [0, 50], "Ingeniería Industrial", "f(x) = e^(-0.1x)"),
        4: (funcion_ingenieria_electromecanica, [0, 40], "Ingeniería Electromecánica", "f(x) = (1-e^(-0.2x)cos(x))/(2(1-e^(-0.2x)cos(40)))"),
        5: (funcion_ingenieria_electronica, [0, 10], "Ingeniería Electrónica", "f(x) = 1/√(1+(x/1)²)"),
        6: (funcion_ingenieria_mecatronica, [0, 2*np.pi], "Ingeniería Mecatrónica", "f(x) = (sin(x) + 0.5cos(2x) + 1.5)/3"),
        7: (funcion_ingenieria_mecanica, [0, 10], "Ingeniería Mecánica", "f(x) = 1/(1+e^(-1(x-5)))")
    }
    
    return funciones[opcion]

def validar_intervalo(limites_default):
    """Valida y permite al usuario ingresar los límites del intervalo"""
    print(f"\nLímites por defecto para esta función: {limites_default}")
    usar_default = input("¿Desea usar los límites por defecto? (s/n): ").lower().strip()
    
    if usar_default == 's' or usar_default == '':
        return limites_default
    else:
        while True:
            try:
                a = float(input("Ingrese el límite inferior (a): "))
                b = float(input("Ingrese el límite superior (b): "))
                if a >= b:
                    print("El límite inferior debe ser menor que el superior")
                    continue
                return [a, b]
            except ValueError:
                print("Por favor ingrese números válidos")

def monte_carlo_area(funcion, a, b, N_valores=[50, 100, 250, 500, 1000]):
    """
    Calcula el área bajo la curva usando el método de Monte Carlo
    para diferentes valores de N
    """
    areas_estimadas = []
    
    for N in N_valores:
        print(f"\nCalculando para N = {N} puntos...")
        
        # Paso 1: Generar puntos aleatorios
        x_random = np.random.uniform(a, b, N)
        y_random = np.random.uniform(0, 1, N)
        
        # Paso 2: Evaluar función en puntos x aleatorios
        fx_values = funcion(x_random)
        
        # Imprimir algunos valores (primeros 5)
        print(f"Primeros 5 valores de f(x): {fx_values[:5]}")
        
        # Paso 3: Contar puntos bajo la curva
        puntos_bajo_curva = np.sum(y_random <= fx_values)
        print(f"Puntos bajo la curva: {puntos_bajo_curva}")
        
        # Paso 4: Calcular área estimada
        area_estimada = (b - a) * (puntos_bajo_curva / N)
        areas_estimadas.append(area_estimada)
        print(f"Área estimada: {area_estimada:.3f}")
    
    return N_valores, areas_estimadas

def graficar_resultados(funcion, a, b, N_valores, areas_estimadas, nombre_carrera, formula):
    """Crea los gráficos requeridos"""
    # Configurar subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfico 1: Método de Monte Carlo con la última generación
    N_final = N_valores[-1]
    x_random = np.random.uniform(a, b, N_final)
    y_random = np.random.uniform(0, 1, N_final)
    fx_values = funcion(x_random)
    
    # Separar puntos bajo y sobre la curva
    bajo_curva = y_random <= fx_values
    
    # Dibujar la función
    x_curva = np.linspace(a, b, 1000)
    y_curva = funcion(x_curva)
    ax1.plot(x_curva, y_curva, 'b-', linewidth=2, label='f(x)')
    
    # Dibujar puntos Monte Carlo
    ax1.scatter(x_random[bajo_curva], y_random[bajo_curva], 
               c='red', alpha=0.6, s=10, label='Puntos bajo la curva')
    ax1.scatter(x_random[~bajo_curva], y_random[~bajo_curva], 
               c='blue', alpha=0.6, s=10, label='Puntos sobre la curva')
    
    ax1.set_xlim(a, b)
    ax1.set_ylim(0, 1)
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.set_title('Método de Montecarlo')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Gráfico 2: Área estimada vs Número de puntos
    ax2.plot(N_valores, areas_estimadas, 'bo-', linewidth=2, markersize=8)
    ax2.set_xlabel('Número de puntos (N)')
    ax2.set_ylabel('Área estimada')
    ax2.set_title('Área estimada vs Número de puntos')
    ax2.grid(True, alpha=0.3)
    
    # Mostrar valores en el gráfico
    for i, (n, area) in enumerate(zip(N_valores, areas_estimadas)):
        ax2.annotate(f'{area:.1f}', (n, area), textcoords="offset points", 
                    xytext=(0,10), ha='center')
    
    plt.tight_layout()
    plt.suptitle(f'{nombre_carrera}\n{formula}', y=1.02)
    plt.show()

def main():
    """Función principal del programa"""
    print("=" * 60)
    print("CÁLCULO DE ÁREA BAJO LA CURVA - MÉTODO DE MONTE CARLO")
    print("Universidad Nacional de Asunción - Facultad de Ingeniería")
    print("=" * 60)
    
    # Paso 1: Selección de función
    funcion, limites_default, nombre_carrera, formula = seleccionar_funcion()
    print(f"\nCarrera seleccionada: {nombre_carrera}")
    print(f"Función: {formula}")
    
    # Paso 2: Entrada de datos (límites del intervalo)
    limites = validar_intervalo(limites_default)
    a, b = limites[0], limites[1]
    print(f"Intervalo de integración: [{a}, {b}]")
    
    # Paso 3: Cálculo del área
    print("\n" + "="*50)
    print("INICIANDO CÁLCULO DE MONTE CARLO")
    print("="*50)
    
    N_valores, areas_estimadas = monte_carlo_area(funcion, a, b)
    
    # Paso 4: Mostrar resultados finales
    print("\n" + "="*50)
    print("RESULTADOS FINALES")
    print("="*50)
    print("N\t\tÁrea Estimada")
    print("-" * 30)
    for n, area in zip(N_valores, areas_estimadas):
        print(f"{n}\t\t{area:.3f}")
    
    # Paso 5: Graficar resultados
    graficar_resultados(funcion, a, b, N_valores, areas_estimadas, 
                       nombre_carrera, formula)
    
    print(f"\nÁrea final estimada con {N_valores[-1]} puntos: {areas_estimadas[-1]:.3f}")

if __name__ == "__main__":
    main()