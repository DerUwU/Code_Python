import math

print("Ingrese Valores para hallar el numero de Reynolds")
velocidad = float(input("Digite la velocidad: "))
diametro = float(input("Digite el diametro: "))
viscosidad = float(input("Digite la viscosidad: "))

numReynolds = (velocidad * diametro) / viscosidad

print("Numero de Reynolds:", numReynolds)

print("Ingrese Valores para hallar la rugosidad relativa")

# Rugosidad Relativa

diametroInterior = float(input("Digite diametro interior: "))
rugosidadAbsoluta = float(input("Digite la rugosidad absoluta: "))

dE = diametroInterior / rugosidadAbsoluta

print("Rugosidad Relativa:", dE)
#a
if numReynolds < 2000:
    print("Ingrese Valores para hallar el factor de friccion para flujo laminar")
    # Factor de friccion para flujo laminar (8-5)

    f85 = 64 / numReynolds

    print("Flujo Laminar:", f85)
#b
elif 2000 < numReynolds < 4000:

    print("El flujo esta en el rango critico y no es posible calcular un valor confiable")

else: #c

    # factor de friccion para flujo turbulento (8-7)

    f87 = 0.25 / ((math.log10((1 / (3.7 * dE)) + (5.74 / (numReynolds ** 0.9)))) ** 2)

    print("Flujo Turbulento:", f87)





