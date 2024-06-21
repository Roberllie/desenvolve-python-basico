caminho_estomago_txt = os.path.join(os.getcwd(), "estomago.txt")

with open(caminho_estomago_txt, 'r', encoding='utf-8') as arquivo:
    linhas_texto = arquivo.readlines()

print("Primeiras 25 linhas:")
print("".join(linhas_texto[:25]))

total_linhas = len(linhas_texto)
print(f"Número de linhas: {total_linhas}")

linha_mais_comprida = max(linhas_texto, key=len)
print(f"Linha com maior número de caracteres: {linha_mais_comprida}")

contador_nonato = sum(1 for linha in linhas_texto if 'nonato' in linha.lower())
contador_iria = sum(1 for linha in linhas_texto if re.search(r'\bíria\b', linha, re.IGNORECASE))

print(f"Menções a 'Nonato': {contador_nonato}")
print(f"Menções a 'Íria': {contador_iria}")
