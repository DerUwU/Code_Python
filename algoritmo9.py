opcion = input("Escriba una operacion algoritmica\nS para sumar\nR para restar\nM o P para multiplicacion\n"
               "D para dividir\n").lower()

if opcion == "s" or opcion == "r" or opcion == "m" or opcion == "p" or opcion == "d":
    if opcion == "s":
        num1 = float(input("Numero 1: "))
        num2 = float(input("Numero 2: "))
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif opcion == "r":
        num1 = float(input("Numero 1: "))
        num2 = float(input("Numero 2: "))
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif opcion == "m" or opcion == "p":
        num1 = float(input("Numero 1: "))
        num2 = float(input("Numero 2: "))
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado:.2f}")
    elif opcion == "d":
        num1 = float(input("Numero 1: "))
        num2 = float(input("Numero 2: "))
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado:.2f}")
    else:
        print("Caracter no valido")
