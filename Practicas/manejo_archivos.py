# filepath: c:\Users\David\Desktop\python\Practicas\manejo_archivos.py

def contar_palabras_archivo():
    """
    Función que lee un archivo de texto y cuenta la cantidad total de palabras.
    Maneja errores como archivo no encontrado y problemas de lectura.
    """
    # Solicitar el nombre del archivo al usuario
    nombre_archivo = input("Ingrese el nombre del archivo .txt a analizar: ")
    
    # Agregar extensión .txt si no la tiene
    if not nombre_archivo.endswith('.txt'):
        nombre_archivo += '.txt'
    
    try:
        # Intentar abrir y leer el archivo
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            
            # Separar las palabras por espacios y filtrar palabras vacías
            palabras = contenido.split()
            
            # Contar las palabras
            cantidad_palabras = len(palabras)
            
            # Mostrar el resultado
            print(f"\nArchivo leído exitosamente: {nombre_archivo}")
            print(f"Cantidad total de palabras encontradas: {cantidad_palabras}")
            
            # Información adicional
            if cantidad_palabras > 0:
                print(f"Primeras 5 palabras: {palabras[:5]}")
                print(f"Últimas 5 palabras: {palabras[-5:]}")
            
    except FileNotFoundError:
        print(f"\nError: El archivo '{nombre_archivo}' no fue encontrado.")
        print("Verifique que el archivo existe y que el nombre esté escrito correctamente.")
        
    except PermissionError:
        print(f"\nError: No tiene permisos para leer el archivo '{nombre_archivo}'.")
        
    except UnicodeDecodeError:
        print(f"\nError: No se pudo leer el archivo '{nombre_archivo}' debido a problemas de codificación.")
        print("El archivo podría contener caracteres especiales o estar en un formato diferente.")
        
    except Exception as e:
        print(f"\nError inesperado al procesar el archivo '{nombre_archivo}': {str(e)}")

def crear_archivo_prueba():
    """
    Función auxiliar para crear un archivo de prueba si es necesario.
    """
    respuesta = input("\n¿Desea crear un archivo de prueba? (s/n): ").lower()
    
    if respuesta == 's':
        nombre_archivo = input("Ingrese el nombre para el archivo de prueba (sin extensión): ")
        contenido_prueba = """Este es un archivo de prueba para contar palabras.
Contiene varias líneas de texto con diferentes palabras.
El programa debería contar todas las palabras correctamente.
¡Prueba el contador de palabras con este archivo!"""
        
        try:
            with open(f"{nombre_archivo}.txt", 'w', encoding='utf-8') as archivo:
                archivo.write(contenido_prueba)
            print(f"Archivo '{nombre_archivo}.txt' creado exitosamente.")
        except Exception as e:
            print(f"Error al crear el archivo: {str(e)}")

def main():
    """
    Función principal del programa.
    """
    print("=== CONTADOR DE PALABRAS EN ARCHIVOS ===")
    print("Este programa lee un archivo de texto y cuenta las palabras que contiene.")
    
    while True:
        print("\nOpciones:")
        print("1. Contar palabras en un archivo")
        print("2. Crear archivo de prueba")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción (1-3): ")
        
        if opcion == '1':
            contar_palabras_archivo()
        elif opcion == '2':
            crear_archivo_prueba()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()