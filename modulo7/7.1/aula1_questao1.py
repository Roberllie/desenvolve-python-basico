#Escreva um programa que solicita o nome do usuário e o imprime em forma de escada
nome = input("Digite seu nome: ")

letras = ""

for letra in nome:
    letras+= letra 
    print(letras)
##outra alternativa 

nome = input("Digite o seu nome: ")

for i in range(len(nome)):
    print(nome[:i])
