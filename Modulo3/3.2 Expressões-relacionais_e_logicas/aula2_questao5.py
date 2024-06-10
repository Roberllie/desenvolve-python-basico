
genero = input("Informe seu gênero (M ou F): ").upper()

idade = int(input("Informe sua idade: "))

tempo_servico = int(input("Informe seu tempo de serviço (em anos): "))

if genero == "F":
    criterio_a = idade > 60
else:
    criterio_a = idade > 65

criterio_b = tempo_servico >= 30
criterio_c = idade >= 60 and tempo_servico >= 25

aposentadoria = criterio_a or criterio_b or criterio_c

print(aposentadoria)
