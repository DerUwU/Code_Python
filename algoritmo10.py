saldoFijo = 1000
print("Numero de Cuenta 1234 2678 9012")
clave = int(input("Clave: "))

if clave == 1126:
    opciones = int(input("Seleccione una opcion:\n"
                         "1. Ingresar dinero a la cuenta\n"
                         "2. Retirar dinero de la cuenta\n"
                         "3. Mostrar dinero disponible\n"
                         "4. Salir\n"
                         "Dijite la opcion que desea consultar: "))

    if opciones == 1:
        saldoAgregar = float(input("Dinero a agregar: "))
        print(f"Agrego satisfactoriamente {saldoAgregar}, su saldo final es de {saldoFijo + saldoAgregar}")
    if opciones == 2:
        saldoQuitar = float(input(f"Actualmente tiene {saldoFijo}, Dinero a retirar: "))
        if saldoFijo > saldoQuitar > 0:
            print(f"Retiro satisfactoriamente {saldoQuitar}, su saldo final es de {saldoFijo - saldoQuitar}")
        elif saldoQuitar > saldoFijo or saldoQuitar < 0:
            print("Error en la transaccion")
    if opciones == 3:
        print(f"Actualmente tiene {saldoFijo} en su cuenta")
    if opciones == 4:
        print("Saliendo de la sesion")

    print("Gracias por utilizar nuestros servicios")

else:
    print("A ingresado erroneamente la contraseña")
