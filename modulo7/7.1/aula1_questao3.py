##Escreva um script que dado uma frase conta os espaços em branco.

frase = input("Digite uma frase: ")
espacos = 0
for i in frase:
    if i == ' ': 
        espacos = espacos + 1 

print("Espaços em branco: ", espacos)
