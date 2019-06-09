'''
    EJEMPLOS TIPO STR
'''


mensaje_1 = "\nRecodar la identación"

mensaje_2 = """
Olvidate del ;
Olvidate del ;
Olvidate del ;
Olvidate del ;
"""

print("Mensaje 1: {}".format(mensaje_1))
print("Mensaje 2: {}".format(mensaje_2))
print("-"*30)


'''
    FORMATEAR CADENAS
'''
val1 , val2, val3 = "Hola", 'Paolo', 23

print("%s. Soy %s y tengo %d.Su valor en hexadecimal es: %x" % (val1, val2, val3, val3))
print("{saludo}. Soy {nombre} y tengo {edad}.\nSu valor en hexadecimal es: {hex}".format(saludo=val1, nombre=val2, edad=val3, hex=hex(23)))
print("-"*30)


