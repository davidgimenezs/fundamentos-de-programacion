num = int(input())

esPrimo = True

if num <= 0:
    print("El numero no es positivo")
    exit()

if num==1:
    esPrimo = False

for i in range(2,num):
    if num%i==0:
        esPrimo = False
        break
    
if esPrimo:
    print(f"El {num} es un numero primo")
else:
    print(f"El {num} no es un numero primo")