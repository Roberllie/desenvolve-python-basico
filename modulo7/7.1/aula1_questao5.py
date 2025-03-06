frase = input("Digite uma frase: ")
vogais= 0
vogais_index = []

for i in range(len(frase)):
    if frase[i] in 'aeiou':
        vogais = vogais + 1
        vogais_index.append(i)

print(vogais)
print(f"Indices: {vogais_index}")
