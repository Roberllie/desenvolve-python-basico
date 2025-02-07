import random

num = random.randint(1,10)
while(True):
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if (palpite == num):
        print(f"Correto! O número é {num}")
        break
    if (palpite > num):
        print("Muito alto, tente novamente!")
    else:
        print("Muito baixo, tente novamente!")
