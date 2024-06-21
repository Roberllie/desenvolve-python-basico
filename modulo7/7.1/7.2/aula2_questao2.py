sentenca = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
sentenca_modificada = ''.join(['*' if caractere in vogais else caractere for caractere in sentenca])

print(f"Frase modificada: {sentenca_modificada}")
