
def asignar_datos(a, b, c):
    dicc = {}
    dicc['nombre']= a
    dicc['edad'] = b
    dicc['ciudad'] = c
    return dicc

def asignar_datos2(**kwargs):
    dicc = {}
    print(kwargs.items())
    print(kwargs.values())
    for i in kwargs.items():
        dicc[i[0]]=i[1]
    return dicc

print("Parametros definidos:")
x = asignar_datos("Paolo", 23, "Lima")
print(x)

print("-"*30)

print("Parametros clave-valor:")
y = asignar_datos2(edad=23, ciudad="Lima", nombre="Paolo")
print(y)
