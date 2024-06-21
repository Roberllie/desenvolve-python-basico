import os

mensagem = input("Digite uma frase: ")

caminho_do_arquivo = os.path.join(os.getcwd(), "frase.txt")

with open(caminho_do_arquivo, 'w') as arquivo:
    arquivo.write(mensagem)

print(f"Frase salva em {caminho_do_arquivo}")

