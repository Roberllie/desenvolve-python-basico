# Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes.
# Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades
# de cada respondente. Ao final, imprima a média das idades.
# (idade1 + idade2 + idade3 + … + idade_n)/

n = int(input("Quantidade de respondentes: "))
cont = 0
soma = 0
while n > cont:
    idade = int(input("Idade: "))
    soma += idade
    cont += 1

media = int(soma / n)
print(f"A media da(s) idade(s) do(s) {n} respondente(s) é {media}")
