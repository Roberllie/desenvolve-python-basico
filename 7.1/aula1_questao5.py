frase = input("Digite uma frase: ")

contador_vogais = 0
indices_vogais = []

for idx, letra in enumerate(frase):
    if letra.lower() in "aeiou":
        contador_vogais += 1
        indices_vogais.append(idx)

print(f"{contador_vogais} vogais")
print(f"Índices {indices_vogais}")
