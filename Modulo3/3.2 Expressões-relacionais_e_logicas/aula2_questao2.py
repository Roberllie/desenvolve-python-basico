#2 - Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa 
#é maior de idade (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando
#as idades de Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo True se puderem 
#entrar no bar, e False caso contrário.

Juliana = int(input("Idade juliana: "))
Cris = int(input("Idade Cris: "))
podem = False 
if (Juliana >17 or Cris >17):
    podem = True
else:
    podem = False 

print(podem)
