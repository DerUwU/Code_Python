examenes_medicos = \
    [[32777584, ("EM_AUD", 15000), ("EM_VIS", 15000), ("EM_FIS", 20000), ("EL_PCOVID", 50000), ("EL_GENERAL", 35000)],
     [1048069255, ("EM_AUD", 15000), ("EM_VIS", 15000), ("EM_FIS", 20000), ("EL_PCOVID", 50000), ("EL_GENERAL", 35000)],
     [8534598, ("EM_AUD", 15000), ("EM_VIS", 15000), ("EM_FIS", 20000)],
     [32444589, ("EM_AUD", 15000), ("EM_VIS", 15000), ("EM_FIS", 20000), ("EL_PCOVID", 50000), ("EL_GENERAL", 35000)]]

dato0 = examenes_medicos[0]
dato1 = examenes_medicos[1]
dato2 = examenes_medicos[2]
dato3 = examenes_medicos[3]

def informe(dato0,dato1,dato2,dato3):
    covid = 0

    cedula = dato0[0]
    if "EL_PCOVID" in dato0[4]:
        covid = + 1
    a = list(map(lambda x, y, z, q, w: x + y + z + q + w, dato0[1], dato0[2], dato0[3], dato0[4], dato0[5]))
    covid = covid + 1
    a.pop(0)
    a.insert(0, cedula)

    cedula = dato1[0]
    if "EL_PCOVID" in dato1[4]:
        covid = + 1
    b = list(map(lambda x, y, z, q, w: x + y + z + q + w, dato1[1], dato1[2], dato1[3], dato1[4], dato1[5]))
    covid = covid + 1
    b.pop(0)
    b.insert(0, cedula)

    cedula = dato2[0]
    c = list(map(lambda x, y, z: x + y + z, dato2[1], dato2[2], dato2[3]))
    c.pop(0)
    c.insert(0, cedula)

    cedula = dato3[0]
    if "EL_PCOVID" in dato3[4]:
        covid = + 1
    d = list(map(lambda x, y, z, q, w: x + y + z + q + w, dato3[1], dato3[2], dato3[3], dato3[4], dato3[5]))
    covid = covid + 1
    d.pop(0)
    d.insert(0, cedula)

    e = [a, b, c, d, covid]
    print(e)


print(informe(dato0,dato1,dato2,dato3))
