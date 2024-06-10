distancia = int(input("Insira a distância da entrega (em km): "))

peso = float(input("Insira o peso do pacote (em kg): "))

if distancia <= 100:
    valor_frete = peso * 1
elif 101 <= distancia <= 300:
    valor_frete = peso * 1.50
else:
    valor_frete = peso * 2

if peso > 10:
    valor_frete += 10

print(f"O valor do frete é R${valor_frete:.2f}")
