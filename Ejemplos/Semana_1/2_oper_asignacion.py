'''
    EJEMPLO OPERADORES DE ASIGNACION
'''

print("-"*30)
print("\tOPERADORES DE ASIGNACIÓN")
print("-"*30)

a, b, c = 16, 10, 0

print("Valor de variable 'a':", a)
print("Valor de variable 'b':", b)

c = a + b
print("Operador = | El valor de variable 'c' es ", c)

c += a
print("Operador += | El valor de variable 'c' es ", c)

c *= a
print("Operador *= | El valor de variable 'c' es ", c)

c /= a
print("Operador /= | El valor de variable 'c' es ", c)

c = 2
c %= a
print("Operador %= | El valor de variable 'c' es ", c)

c **= a
print("Operador **= | El valor de variable 'c' es ", c)

c //= a
print("Operador //= | El valor de variable 'c' es ", c)