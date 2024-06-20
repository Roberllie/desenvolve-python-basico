import random

lista = [random.randint(-10, 10) for _ in range(20)]

print("Original:", lista)

maior_qtd_negativos = []
for i in range(len(lista)):
    if lista[i] < 0:
        qtd_negativos = 1
        for j in range(i + 1, len(lista)):
            if lista[j] < 0:
                qtd_negativos += 1
            else:
                break
        if len(maior_qtd_negativos) == 0 or qtd_negativos > len(maior_qtd_negativos):
            maior_qtd_negativos = lista[i:i + qtd_negativos]

if maior_qtd_negativos:
    lista = [num for num in lista if num not in maior_qtd_negativos]

print("Editada: ", lista)
