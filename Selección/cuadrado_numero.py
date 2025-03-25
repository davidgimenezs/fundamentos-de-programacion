numero = input()

if "." in numero and float(numero) < 0:
    print("Error, el numero ingresado no es entero ni positivo")
elif "." in numero:
    print("Error, el numero ingresado no es entero")
elif float(numero) < 0:
    print("Error, el numero ingresado no es positivo")
elif float(numero) >= 10000:
    print("Error, el numero ingresado es muy grande")
    
else:
    numero = int(float(numero))
    print(numero * numero)