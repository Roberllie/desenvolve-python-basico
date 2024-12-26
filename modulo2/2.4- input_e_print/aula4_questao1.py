# programa que calcula as dimen~soes e preço de um terreno

# solicita ao usuário e guarda os valores do terreno e o preço do metro quadrado
comprimento = int(input("Comprimento: "))
largura = int(input("Largura: "))
preco_m2 = float(input("Preço do m/2: "))

# calcula a área do terreno
area_m2 = comprimento * largura

# calculca preço total do terreno
preco_total = area_m2 * preco_m2

#Impressão formatada 
print(f"O terreno possui {area_m2}m2 e custa {preco_total:,.2f} reais")
