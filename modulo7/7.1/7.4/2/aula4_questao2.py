import re

caminho_da_frase = os.path.join(os.getcwd(), "frase.txt")

with open(caminho_da_frase, 'r') as arquivo:
    conteudo_frase = arquivo.read()

lista_palavras = re.findall(r'\b\w+\b', conteudo_frase)

caminho_do_palavras = os.path.join(os.getcwd(), "palavras.txt")

with open(caminho_do_palavras, 'w') as arquivo:
    for palavra in lista_palavras:
        arquivo.write(palavra + '\n')

with open(caminho_do_palavras, 'r') as arquivo:
    print(arquivo.read())
