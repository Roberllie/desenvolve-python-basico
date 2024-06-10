# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

jogou_tres_jogos_str = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ")
jogou_tres_jogos = jogou_tres_jogos_str == "True"


vitorias = int(input("Quantos jogos já venceu? "))

idade_valida = 16 <= idade <= 18

jogos_validos = jogou_tres_jogos

vitorias_validas = vitorias > 0

apto = idade_valida and jogos_validos and vitorias_validas

print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto}")
