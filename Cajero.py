dineroAb = int(input("Ingrese la cantidad a sacar: "))
print(dineroAb)

dineroCaj = dineroAb

if dineroCaj > 0:
    aux = (dineroCaj/100)
    print("Cantidad de billetes de 100 es: ",int(aux))

    aux2 = (dineroCaj%100)/50
    print("Cantidad de billetes de 50 es: ",int(aux2))

    aux3 = ((dineroCaj%100)%50)/20
    print("Cantidad de billetes de 20 es: ", int(aux3))

    aux4 = ((((dineroCaj % 100) % 50) % 20) /10)
    print("Cantidad de billetes de 10 es: ", int(aux4))

    aux5 = (((((dineroCaj % 100) % 50) % 20) % 10) /5)
    print("Cantidad de billetes de 5 es: ", int(aux5))

    aux6 = ((((((dineroCaj % 100) % 50) % 20) % 10) % 5)/2)
    print("Cantidad de billetes de 2 es: ", int(aux6))

    aux7 = (((((((dineroCaj % 100) % 50) % 20) % 10) % 5) % 2) / 1)
    print("Cantidad de billetes de 1 es: ", int(aux7))


