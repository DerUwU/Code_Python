edad = int(input("Digite su edad: "))

if 0 < edad < 100:
    print(f"La edad {edad} es valida")
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

else:
    print(f"La edad {edad} es incorrecta")
