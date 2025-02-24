import random
lista =[]

for i in range(20):
    lista.append(random.randint(-100,100))

maximo = max(lista)
minimo = min(lista)


print(sorted(lista)) ##imprime a lista em ordem sem modificá-la, com a função embutida sorted 
print(lista)
print(f"O índice do maior número é {lista.index(maximo)} que é {maximo}")
print(f"O índice do menor número é {lista.index(minimo)} que é {minimo}")
