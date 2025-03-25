tarifa_diurna = 10000
tarifa_nocturna = 20000
tarifa_domingo = 1.25

dia_trabajo = int(input())
horas_diurnas = float(input())
horas_nocturnas = float(input())

jornal = tarifa_diurna*horas_diurnas + tarifa_nocturna*horas_nocturnas

if dia_trabajo == 7: #Domingo
    print(int(jornal*tarifa_domingo))
else:
    print(int(jornal))