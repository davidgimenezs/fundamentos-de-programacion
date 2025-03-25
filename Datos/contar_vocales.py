texto = input()

vocales = "aeiouAEIOU"
cantidad_vocales = 0

for letra in texto:
    if letra in vocales:
        cantidad_vocales += 1

print(f"La palabra ingresada contiene: {cantidad_vocales} vocales")
