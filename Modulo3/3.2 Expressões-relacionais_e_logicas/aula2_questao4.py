
idade = int(input("Digite sua idade: "))

classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").lower()

forca = int(input("Digite os pontos de força (de 1 a 20): "))

magia = int(input("Digite os pontos de magia (de 1 a 20): "))


if classe == "guerreiro":
    forca_valida = forca >= 15
    magia_valida = magia <= 10
    atributos_validos = forca_valida and magia_valida
elif classe == "mago":
    forca_valida = forca <= 10
    magia_valida = magia >= 15
    atributos_validos = forca_valida and magia_valida
elif classe == "arqueiro":
    forca_valida = 5 < forca <= 15
    magia_valida = 5 < magia <= 15
    atributos_validos = forca_valida and magia_valida
else:
    atributos_validos = False


print(f"Pontos de atributo consistentes com a classe escolhida: {atributos_validos}")
