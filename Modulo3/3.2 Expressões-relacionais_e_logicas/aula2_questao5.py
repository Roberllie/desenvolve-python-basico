#Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma 
# expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as 
# seguintes regras:
#A: Para mulheres, ter mais de 60 anos. Para homens, 65.
#B: Ou ter trabalhado pelo menos 30 anos
#C: Ou ter 60 anos  e trabalhado pelo menos 25.

genero = input("Genero(f/m): ")
idade = int(input("Idade: "))
tempo = int(input("Tempo de serviço: "))
aposentar = False

if (idade >= 60 and tempo >= 25):
    aposentar = True

elif genero == 'm':
    aposentar = bool(idade > 60)


elif genero == 'f':
    aposentar = bool(idade > 65 or tempo >= 30)

print(f"Aposentar: {aposentar}")
