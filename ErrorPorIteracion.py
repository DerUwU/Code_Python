from math import factorial

# 1 Funcion
print("PRIMERA FUNCION")

x = float(input("Ingresa el numero para empezar: "))
e = 2.718
auxAuxEx = []
auxAuxEr = []
auxAuxEa = []
auxAuxTer = []

fun = e ** x

print("Valor Verdadero: ", fun)

es = (0.5 * (10 ** (2 - 3)))
print("Nivel de tolerancia 3 terminos es: ", es, "%")

ex1 = (1 + x)
print("e^", x, "=", ex1)
auxAuxEx.insert(0, ex1)

er = ((fun - ex1) / fun) * 100
print("Error Relativo: ", er)
auxAuxEr.insert(0, er)

ea = ((ex1 - 1) / ex1) * 100
print("Error Absoluto: ", ea)
auxAuxEa.insert(0, ea)


num = 2
num2 = 1
num3 = 1
repVeces = int(input("¿Cuantas veces se debe repetir la iteracion?"))

for i in range(repVeces):

    auxEx = auxAuxEx[i] + ((x ** num) / factorial(num))
    auxAuxEx.append(auxEx)
    num = num + +1

    auxEr = ((fun - auxAuxEx[num2]) / fun) * 100
    auxAuxEr.append(auxEr)
    num2 = num2 + +1

    auxEa = ((auxAuxEx[num3] - auxAuxEx[i]) / auxAuxEx[num3]) * 100
    auxAuxEa.append(auxEa)
    num3 = num3 + +1

    if abs(auxEa) <= 0.0001:
        print("El valor se encontro en: ", i)
        print(auxAuxEx[i])
        print(auxAuxEr[i])
        print(auxAuxEa[i])
    else:
        print("No se encontro")

# 2 Funcion
print("SEGUNDA FUNCION")

x = float(input("Ingresa el numero para empezar: "))
e = 2.718
auxAuxEx2 = []
auxAuxEr2 = []
auxAuxEa2 = []
auxAuxTer2 = []

fun2 = 1/(e ** x)

print("Valor Verdadero: ", fun)

es = (0.5 * (10 ** (2 - 3)))
print("Nivel de tolerancia 3 terminos es: ", es, "%")

ex1 = (1 + x)
print("e^", x, "=", ex1)
auxAuxEx2.insert(0, ex1)

er = ((fun - ex1) / fun) * 100
print("Error Relativo: ", er)
auxAuxEr2.insert(0, er)

ea = ((ex1 - 1) / ex1) * 100
print("Error Absoluto: ", ea)
auxAuxEa2.insert(0, ea)

auxcon = []

nuM = 2
nuM2 = 1
nuM3 = 1
repVeces = int(input("¿Cuantas veces se debe repetir la iteracion?"))

for i in range(repVeces):

    auxEx2 = (auxAuxEx2[i] + ((x ** nuM) / factorial(nuM)))
    auxEx2 = 1/auxEx2
    auxAuxEx2.append(auxEx2)
    nuM = nuM + +1

    auxEr2 = ((fun2 - auxAuxEx2[nuM2]) / fun2) * 100
    auxAuxEr2.append(auxEr2)
    nuM2 = nuM2 + +1

    auxEa2 = ((auxAuxEx2[nuM3] - auxAuxEx2[i]) / auxAuxEx2[nuM3]) * 100
    auxAuxEa.append(auxEa)
    nuM3 = nuM3 + +1

    if abs(auxEa2) <= 0.0001:
        print("El valor se encontro en: ", i)
        print(auxAuxEx2[i])
        print(auxAuxEr2[i])
        print(auxAuxEa2[i])
    else:
        print("No se encontro")
