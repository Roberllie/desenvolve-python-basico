numero = input("Digite um número: ")
if len(numero) == 8:
    numero = '9'+numero 
if len(numero) == 9:
        num_sepa = numero[:5]+"-"+numero[5:]
        print(num_sepa)
