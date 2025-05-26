def validar(cadena):
    promedio = float(input(cadena))
    while promedio < 1 or promedio > 5:
        promedio = float(input(cadena))
    return promedio

def cargarunalumno(alumno):
    alumno['nombre_completo'].append(input('Ingrese el Apellido, Nombre: '))
    alumno['semestre'].append(int(input('Ingrese el semestre: ')))
    alumno['promedio'].append(validar('Ingrese el promedio: '))

def cargarnalumnos(alumno, n):
    for i in range(n):
        print(f'\nIngrese los datos del alumno {i+1}')
        cargarunalumno(alumno)

def imprimiralumnos(alumno):
    n = len(alumno['nombre_completo'])
    print('\n\nNombre\t\tApellido\tSemestre\tPromedio') 
    
    for i in range(n):
        nombre = alumno['nombre_completo'][i].split(', ')[1]
        apellido = alumno['nombre_completo'][i].split(', ')[0]
        semestre = alumno['semestre'][i]
        promedio = alumno['promedio'][i]
        print(f'{nombre}\t\t{apellido}\t\t{semestre}\t\t{promedio}')

def intercambio(diccionario, i, j):
    lista = list(diccionario.keys())
    for k in lista:
        diccionario[k][i], diccionario[k][j] = diccionario[k][j], diccionario[k][i]


def ordenaralumnos(alumno, clave):
    n = len(alumno[clave])
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if alumno[clave][i] < alumno[clave][j]:
                intercambio(alumno, i, j)
                i = i - 1

def nomalizarnombreapellido(alumno):
    n = len(alumno['nombre_completo'])
    for i in range(n):
        alumno['nombre_completo'][i] = alumno['nombre_completo'][i].split(', ')[0][0].upper() + alumno['nombre_completo'][i].split(', ')[0][1:] + ', ' + alumno['nombre_completo'][i].split(', ')[1][0].upper() + alumno['nombre_completo'][i].split(', ')[1][1:]


alumno = {'nombre_completo': [],
          'semestre': [],
          'promedio': []}

N = int(input('Ingrese la cantidad de alumnos: '))

cargarnalumnos(alumno, N)
# imprimiralumnos(alumno)
ordenaralumnos(alumno, 'nombre_completo')
ordenaralumnos(alumno, 'promedio')
ordenaralumnos(alumno, 'semestre')

nomalizarnombreapellido(alumno)
imprimiralumnos(alumno)