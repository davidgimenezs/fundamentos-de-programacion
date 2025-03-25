n = int(input())

menores=0
mayores=0
i=0

for i in range(0,n,1):
    a = int(input())
    if a >= 18:
        mayores+=1
    else:
        menores+=1

mayores=int((mayores/n)*100)
menores=int((menores/n)*100)

print(f"Mayores de edad:{mayores}% Menores de edad:{menores}%")
