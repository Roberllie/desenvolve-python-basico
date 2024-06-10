# Solicita ao usuário os dados do produto 1
produto1_nome = input("Informe o nome do produto 1: ")
produto1_preco_unitario = float(input("Informe o preço unitário do produto 1: "))
produto1_quantidade = int(input("Informe a quantidade do produto 1: "))

# Solicita ao usuário os dados do produto 2
produto2_nome = input("Informe o nome do produto 2: "))
produto2_preco_unitario = float(input("Informe o preço unitário do produto 2: "))
produto2_quantidade = int(input("Informe a quantidade do produto 2: "))

# Solicita ao usuário os dados do produto 3
produto3_nome = input("Informe o nome do produto 3: ")
produto3_preco_unitario = float(input("Informe o preço unitário do produto 3: "))
produto3_quantidade = int(input("Informe a quantidade do produto 3: "))

# Calcula o valor total de cada produto
produto1_total = produto1_preco_unitario * produto1_quantidade
produto2_total = produto2_preco_unitario * produto2_quantidade
produto3_total = produto3_preco_unitario * produto3_quantidade

# Soma os valores totais dos produtos para obter o preço total da compra
preco_total_compra = produto1_total + produto2_total + produto3_total

# Exibe o resultado formatado
print(f"Total: R${preco_total_compra:,.2f}")
