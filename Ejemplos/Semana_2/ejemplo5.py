
lista = [1,2,3,4,5]
print(lista)

print("\nForma 1:")
tmp = []
for i in lista:
    tmp.append(i*2)
print(tmp)

print("Con Map:")
tmp2 = list(map(lambda x: x, {'nombre':'Paolo','edad':22}.items()))
print(tmp2)

print("Filter:")
tmp3 = list(filter(lambda x: x*3, lista))
print(tmp3)