n = int(input())
entrada = input().split()
l1 = [int(x) for x in entrada]

l2 = []
contador = {}
i = 0

while i < len(l1):
    num = l1[i]
    if num not in contador:
        contador[num] = 1
        l2.append(num)
    else:
        contador[num] += 1
    i += 1

i = 0
while i < len(l2):
    num = l2[i]
    print(num, contador[num], end=" ")
    i += 1
