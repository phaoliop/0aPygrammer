lista = []
print("For:")
for i in range(5):
    sublista = []
    for j in range(5):
        sublista.append(j)
    lista.append(sublista)

for l in lista:
    print(l)

print("Iterador:")
lista2 = [i for i in [[x for x in range(5)] for j in range(5)]]
for l in lista2:
    print(l)