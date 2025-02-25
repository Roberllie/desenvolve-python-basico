import random 

tan = int(input("Tamanho da lista igual ou acima de 4: "))
lista = []
for i in range(4):
    
    lista.append(random.randint(0,100))

print(lista)
print(lista[0:3])
print(lista[:-3:-1])
print(lista[::-1])
print(lista[0:tan:2])
print(lista[1:tan:2])
