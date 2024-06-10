
juliana_idade = int(input("Informe a idade de Juliana: "))
cris_idade = int(input("Informe a idade de Cris: "))

juliana_maior_de_idade = juliana_idade > 17
cris_maior_de_idade = cris_idade > 17

podem_entrar = juliana_maior_de_idade or cris_maior_de_idade

print(podem_entrar)
