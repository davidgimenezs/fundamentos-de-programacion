numero = input()
es_binario = True

for digito in numero:
    if digito != "0" and digito != "1":
        es_binario = False
        break 

if es_binario:
    print("Es un numero binario")
else:
    print("No es un numero binario")
