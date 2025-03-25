P=int(input()) #cantidad principal
r=int(input()) #tasa de interes
n=int(input()) #numero de años

A=P*(1+(r/100))**n

print(f"La cantidad final después de {n} años es: ${A}")