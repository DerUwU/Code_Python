num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

if num1%2 == 0 and num2%2 == 0:
    print("Ambos son pares")
elif num1%2 == 0 and num2%2 != 0:
    print(f"El primer numero ({num1}) Es par")
elif num2%2 == 0 and num1%2 != 0:
    print(f"El segundo numero ({num2}) Es par")
else:
    print("Ninguno es par")
