# input do terreno, comprimento e largura, e o preço por metro quadrado
comprimento = int(input("Comprimento do terreno (m): "))
largura = int(input("Largura do terreno (m): "))
preco_metro2 = float(input("Preço do metro quadrado: "))

# Calcular a área do terreno
area_metro2 = comprimento * largura

# Cálculo do preço total do terreno
preco_total = preco_metro2 * area_metro2

# Impressão do resultado formatado
print(f"O terreno possui {area_metro2}m2 e custa R${preco_total:,.2f}")
