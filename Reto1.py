dicSalida = {'nombre': 'Juan', 'apellido': 'Castro', 'id': 32778569,
               'salario_neto': 945000, 'ventas': 2130000}

def pago_mensual():

    if dicSalida['ventas'] <= 1000000:
        comision = dicSalida['ventas']*0.03
        comision = comision + dicSalida['salario_neto']
        dicSalida.setdefault('pagoTotal', comision)
        dicSalida.setdefault('felicitacion', "No")

    else:
        if dicSalida['ventas'] >= 1000001 and dicSalida['ventas']<=3000000:
            comision = dicSalida['ventas'] * 0.05
            comision = comision + dicSalida['salario_neto']
            dicSalida.setdefault('pagoTotal', comision)
            dicSalida.setdefault('felicitacion', "No")

        elif dicSalida['ventas'] >= 3000001 and dicSalida['ventas']<=5000000:
            comision = dicSalida['ventas'] * 0.08
            comision = comision + dicSalida['salario_neto']
            dicSalida.setdefault('pagoTotal', comision)
            dicSalida.setdefault('felicitacion', "No")

        elif dicSalida['ventas'] >= 5000001 and dicSalida['ventas']<=10000000:
            comision = dicSalida['ventas'] * 0.12
            comision = comision + dicSalida['salario_neto']
            dicSalida.setdefault('pagoTotal', comision)
            dicSalida.setdefault('felicitacion', "No")

        elif dicSalida['ventas'] > 10000000:
            comision = dicSalida['ventas'] * 0.12
            comision = comision + dicSalida['salario_neto']
            dicSalida.setdefault('pagoTotal', comision)
            dicSalida.setdefault('felicitacion', "Si")

    print (f"El pago mensual de {dicSalida['nombre']} {dicSalida['apellido']} identificado con {dicSalida['id']} es: "
           f"{dicSalida['pagoTotal']}. Felicitaciones por ventas: {dicSalida['felicitacion']}")

print(pago_mensual())