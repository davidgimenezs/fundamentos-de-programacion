d1 = int(input())
m1 = int(input())
a1 = int(input())
d2 = int(input())
m2 = int(input())
a2 = int(input())

fecha1 = (a1, m1, d1)
fecha2 = (a2, m2, d2)

if fecha1 > fecha2:
    print("La fecha 1 es más reciente")
elif fecha1 < fecha2:
    print("La fecha 2 es más reciente")
else:
    print("Las fechas son iguales")
