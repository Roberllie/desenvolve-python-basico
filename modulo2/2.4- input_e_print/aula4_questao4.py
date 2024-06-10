# Solicita ao usuário o valor em reais
valor = int(input("Informe um valor em reais: "))

# Calcula a quantidade de notas de 100 reais necessárias
notas_100 = valor // 100
valor %= 100

# Calcula a quantidade de notas de 50 reais necessárias
notas_50 = valor // 50
valor %= 50

# Calcula a quantidade de notas de 20 reais necessárias
notas_20 = valor // 20
valor %= 20

# Calcula a quantidade de notas de 10 reais necessárias
notas_10 = valor // 10
valor %= 10

# Calcula a quantidade de notas de 5 reais necessárias
notas_5 = valor // 5
valor %= 5

# Calcula a quantidade de notas de 2 reais necessárias
notas_2 = valor // 2
valor %= 2

# Calcula a quantidade de notas de 1 real necessárias
notas_1 = valor // 1

# Exibe o resultado formatado
print(f"{notas_100} nota(s) de R$100,00")
print(f"{notas_50} nota(s) de R$50,00")
print(f"{notas_20} nota(s) de R$20,00")
print(f"{notas_10} nota(s) de R$10,00")
print(f"{notas_5} nota(s) de R$5,00")
print(f"{notas_2} nota(s) de R$2,00")
print(f"{notas_1} nota(s) de R$1,00")
