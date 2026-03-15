# Ivereter uma lista sem usar reverse

lista = [1, 2, 3, 4]
invertida = []
for i in lista:
    invertida = [i] + invertida
print(invertida)


# Remover números negativos de uma lista

lista = [5, -2, 7, -1]
positivos = []
for n in lista:
    if n >= 0:
        positivos.append(n)
print(positivos)