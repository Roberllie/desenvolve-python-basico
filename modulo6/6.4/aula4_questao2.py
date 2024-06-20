frase = input("Digite uma frase: ")

vogais = 'aeiouAEIOU'

lista_vogais = [char for char in frase if char in vogais]
lista_consoantes = [char for char in frase if char.isalpha() and char not in vogais]

print("Vogais:", sorted(lista_vogais))
print("Consoantes:", lista_consoantes)
