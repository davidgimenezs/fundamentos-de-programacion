n=10
i=0
impares=0
pares=0
docena=0
mayor=0
ceros=0
suma=0

for i in range(0,n,1):
    num = int(input())
    if num % 2 == 0:
        if num != 0:
            pares+=1
            suma+=num
        else:
            ceros+=1
    else:
        impares+=1
    if num >= 13 and num <= 24:
        docena+=1
    if num > mayor:
        mayor = num

pares=(suma/pares)

print(f"a={impares}\nb={pares:.1f}\nc={docena}\nd={mayor}")