#Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
#Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
#Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.
#Escolha a classe (guerreiro, mago ou arqueiro): mago

#Digite os pontos de força (de 1 a 20): 8

#Digite os pontos de magia (de 1 a 20): 17

#Pontos de atributo consistentes com a classe escolhida: True

classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")

forca = int(input("Digite os pontos de força (de 1 a 20): "))

magia = int(input("Digite os pontos de magia (de 1 a 20): "))

consistente = False 

if (classe == 'guerreiro'):
        consistente = bool((forca >= 15 and magia <= 10))

elif (classe == 'mago'):
    consistente = bool((magia >= 15 and forca <= 10))

elif (classe == 'arqueiro'):
    consistente = bool((magia >= 5 and magia >= 15 and forca >= 5 and forca <= 15))

print(f"Pontos de atributo consistentes com a classe escolhida: {consistente}")




