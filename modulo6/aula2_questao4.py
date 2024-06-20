def intercalar_listas(lista1, lista2):
    tamanho1 = len(lista1)
    tamanho2 = len(lista2)
    resultado = []

    for i in range(max(tamanho1, tamanho2)):
        if i < tamanho1:
            resultado.append(lista1[i])
        if i < tamanho2:
            resultado.append(lista2[i])

    return resultado

quantidade1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input(f"Digite o {i+1}º elemento da lista 1: ")) for i in range(quantidade1)]

quantidade2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input(f"Digite o {i+1}º elemento da lista 2: ")) for i in range(quantidade2)]

lista_intercalada = intercalar_listas(lista1, lista2)

print("Lista intercalada:", " ".join(map(str, lista_intercalada)))
