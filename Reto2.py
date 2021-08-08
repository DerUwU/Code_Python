inmu = [{'año': 2002, 'm2': 100, 'asc': True, 'gar': True, 'hab': 3, 'zona': 3},
        {'año': 1985, 'm2': 80, 'asc': True, 'gar': True, 'hab': 3, 'zona': 4},
        {'año': 2006, 'm2': 90, 'asc': False, 'gar': True, 'hab': 3, 'zona': 5},
        {'año': 2012, 'm2': 180, 'asc': True, 'gar': True, 'hab': 4, 'zona': 2},
        {'año': 1999, 'm2': 70, 'asc': False, 'gar': True, 'hab': 3, 'zona': 1},
        {'año': 2003, 'm2': 220, 'asc': True, 'gar': True, 'hab': 5, 'zona': 6}]

inmu0 = inmu[4]
inmu1 = inmu[3]
inmu2 = inmu[0]
inmu3 = inmu[1]
inmu4 = inmu[2]
inmu5 = inmu[5]

presupuesto = int(input("Escriba su presupuesto: "))

def buscar():

    if inmu0['zona'] == 1:
        pre = 0
        if inmu0['gar'] == True:
            pre = pre + 5000000
        if inmu0['asc'] == True:
            pre = pre + 1500000
    pre = pre + (inmu0['m2'] * 800000)
    pre = pre + (inmu0['hab']*1000000)
    pre = pre * (1 - (2021 - inmu0['año'])/100)
    dict(inmu0)
    inmu0.setdefault('pre', pre)

    if inmu1['zona'] == 2:
        pre = 0
        if inmu1['gar'] == True:
            pre = pre + 5000000
        if inmu1['asc'] == True:
            pre = pre + 1500000
    pre = pre + (inmu1['m2'] * 1200000)
    pre = pre + (inmu1['hab']*1000000)
    pre = pre * (1 - (2021 - inmu1['año'])/100)
    dict(inmu1)
    inmu1.setdefault('pre', pre)

    if inmu2['zona'] == 3:
        pre = 0
        if inmu2['gar'] == True:
            pre = pre + 5000000
        if inmu2['asc'] == True:
            pre = pre + 1500000
    pre = pre + (inmu2['m2'] * 2200000)
    pre = pre + (inmu2['hab']*1000000)
    pre = pre * (1 - (2021 - inmu2['año'])/100)
    dict(inmu2)
    inmu2.setdefault('pre', pre)

    if inmu3['zona'] == 4:
        pre = 0
        if inmu3['gar'] == True:
            pre = pre + 5000000
        else:
            pre = pre
        if inmu3['asc'] == True:
            pre = pre + 1500000
        else:
            pre = pre
    pre = pre + (inmu3['m2'] * 3400000)
    pre = pre + (inmu3['hab']*1000000)
    pre = pre * (1 - (2021 - inmu3['año'])/100)
    dict(inmu3)
    inmu3.setdefault('pre', pre)

    if inmu4['zona'] == 5:
        pre = 0
        if inmu4['gar'] == True:
            pre = pre + 5000000
        if inmu4['asc'] == True:
            pre = pre + 1500000
    pre = pre + (inmu4['m2'] * 5200000)
    pre = pre + (inmu4['hab']*1000000)
    pre = pre * (1 - (2021 - inmu4['año'])/100)
    dict(inmu4)
    inmu4.setdefault('pre', pre)

    if inmu5['zona'] == 6:
        pre = 0
        if inmu5['gar'] == True:
            pre = pre + 5000000
        if inmu5['asc'] == True:
            pre = pre + 1500000
    pre = pre + (inmu5['m2'] * 6400000)
    pre = pre + (inmu5['hab']*1000000)
    pre = pre * (1 - (2021 - inmu5['año'])/100)
    dict(inmu5)
    inmu5.setdefault('pre', pre)

    if presupuesto <= pre:
        print(inmu0)
    if presupuesto <= pre:
        print(inmu1)
    if presupuesto <= pre:
        print(inmu2)
    if presupuesto <= pre:
        print(inmu3)
    if presupuesto <= pre:
        print(inmu4)
    if presupuesto <= pre:
        print(inmu5)

print(buscar())