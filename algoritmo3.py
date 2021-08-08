a = int(input("Variable a: "))
b = int(input("Variable b: "))

# Metodo con lo de Java

aux = a
a = b
b = aux

print(f"La variable a es {a} y la variable b es {b} y aux es {aux}")

# Metodo Pro con algoritmo de Python

a, b = b, a

print(f"La variable a es {a} y la variable b es {b}")
