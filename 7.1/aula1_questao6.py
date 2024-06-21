from collections import Counter

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

palavras = frase.replace(",", "").replace(".", "").split()

anagramas = []
objetivo_counter = Counter(palavra_objetivo.lower())

for palavra in palavras:
    palavra_counter = Counter(palavra.lower())
    if palavra_counter == objetivo_counter and palavra.lower() != palavra_objetivo.lower():
        anagramas.append(palavra)

print(f"Anagramas: {anagramas}")
