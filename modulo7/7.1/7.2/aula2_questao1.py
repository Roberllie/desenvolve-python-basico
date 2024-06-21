data_nasc = input("Digite uma data de nascimento (dd/mm/aaaa): ")

nomes_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
               "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

dia, mes, ano = data_nasc.split('/')

mes_por_extenso = nomes_meses[int(mes) - 1]

print(f"Você nasceu em {dia} de {mes_por_extenso} de {ano}.")

