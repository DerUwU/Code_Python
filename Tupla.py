tupla = (1, 2, 3, 4)

print(tupla.count(1))
print(tupla.index(1))
print(len(tupla))
print(tupla[:])
print(tupla[1:3])
print(tupla[3])

lista = list(tupla)

print(lista[:])

tupla = tuple(lista)

print(tupla[:])
