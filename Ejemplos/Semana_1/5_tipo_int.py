'''
    EJEMPLO TIPO int
'''

a = 10 #Decimal
b = 0x10 #Hexadecimal
c = 0o10 #Octal
d = 0b1111 #Binario


print("-"*60)
print("\tTIPO DE DATO int")
print("-"*60)

print(type(a), type(b), type(c), type(d))
print('Valor de a: {} \nValor de b: {}\nValor de c: {}\nValor de d: {}'.format(a, b, c, d))

#Cast / Conversiones

cadena_num = '0b1111'
mi_num = 10

print("-"*60)
print("De String a Int: {}".format(int(cadena_num,2)))
print("A Hexadecimal: {}".format(hex(mi_num)))
print("A Octal: {}".format(oct(mi_num)))
print("A binario: {}".format(bin(mi_num)))


'''
    TIPO FLOAT
'''

num = 33.45
print("-"*30)
print(type(num))
print(num)

cadena_float = "10.4"
print("Float: {}".format(float(cadena_float)))


'''
    TIPO COMPLEJO
'''

num = 3.5 + 4j
print("-"*30)
print(type(num))
print(num)