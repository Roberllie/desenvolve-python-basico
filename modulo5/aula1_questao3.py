import random

numero_aleatorio = random.randint(1, 10)

palpite = None

while palpite != numero_aleatorio:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))

    if palpite > numero_aleatorio:
        print("Muito alto, tente novamente!")
    elif palpite < numero_aleatorio:
        print("Muito baixo, tente novamente!")
    else:
        print(f"Correto! O número é {numero_aleatorio}.")
