lista = [1, 2, 4, 5]

lista.append("Der") #Lo pone al final de la lista
lista.insert(2, 3) #Pone un valor en un index que se determine
lista.extend([6, 7, 8]) #Pone esos valores al final, debe ser otra lista

lista2 = [9, 10, 11, 10]

lista3 = lista+lista2 #Suma de listas

print("Primera Lista", lista)
print("Segunda Lista", lista2)
print("Tercera Lista", lista3)

print("Der" in lista3) #False o True depende si se encuentra en la lista
print(lista3.index("Der")) #Indice del elemento que se pone
print(lista3.count("Der")) #Contar cuantas veces un elemento se encuentra en la lista
print(lista3.pop()) #Elimina el ultimo valor de la lista
print(lista3.pop(0)) #Elimina el valor en la posicion que esta entre los parentesis
print(lista3.remove(10)) #Elimina un valor especifico de la lista, aunque este repetido
#print(lista3.clear()) #Vacia una lista
print(lista3.reverse()) #Poner al revez la lista
print(lista3.sort()) #Ordena ascendenetemente
print(lista3.sort(reverse=True)) #Ordena descendentemente

print(lista3)
