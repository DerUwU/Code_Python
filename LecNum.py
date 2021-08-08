numList = []

for i in range(10):
    num = int(input(f"Coloque el {i+1} numero: "))
    numList.append(num)

mayor = max(numList, key=int)
pos = numList.index(mayor)


print("El mayor numero es: ", mayor)
print("Esta en la posicion ",pos)
