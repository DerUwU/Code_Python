num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = int(input("Numero 3: "))

if num1 >= num2 and num1 >= num3:
        print(f"El primer numero {num1} es el mayor de todos")
elif num2 >= num1 and num2 >= num3:
    print(f"El segundo numero {num2} es el mayor de todos")
elif num3 >= num1 and num2 >= num2:
    print(f"El tercer numero {num3} es el mayor de todos")