import random

def desenha_enforcado(erros):
    with open("gabarito_enforcado.txt", 'r') as arquivo:
        estados = arquivo.read().splitlines()
    print(estados[erros])

with open("gabarito_forca.txt", 'r') as arquivo:
    lista_palavras = arquivo.read().splitlines()

palavra_sorteada = random.choice(lista_palavras).lower()
estado_palavra = ['_' for _ in palavra_sorteada]

erros_jogador = 0
letras_erradas = set()
letras_certas = set()

while erros_jogador < 6 and ''.join(estado_palavra) != palavra_sorteada:
    print(f"Palavra: {' '.join(estado_palavra)}")
    tentativa = input("Digite uma letra: ").lower()

    if tentativa in letras_erradas or tentativa in letras_certas:
        print("Você já tentou essa letra. Tente outra.")
    elif tentativa in palavra_sorteada:
        letras_certas.add(tentativa)
        for i, letra in enumerate(palavra_sorteada):
            if letra == tentativa:
                estado_palavra[i] = tentativa
    else:
        letras_erradas.add(tentativa)
        erros_jogador += 1
        desenha_enforcado(erros_jogador)

if ''.join(estado_palavra) == palavra_sorteada:
    print(f"Parabéns! Você adivinhou a palavra: {palavra_sorteada}")
else:
    print(f"Você perdeu! A palavra era: {palavra_sorteada}")
