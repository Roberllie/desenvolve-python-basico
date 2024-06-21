def valida_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    
    if not cpf.isdigit() or len(cpf) != 11:
        return False
    
    soma = 0
    multiplicador = 10
    for i in range(9):
        soma += int(cpf[i]) * multiplicador
        multiplicador -= 1
    resto = soma % 11
    digito_verificador1 = 0 if resto < 2 else 11 - resto
    
    if int(cpf[9]) != digito_verificador1:
        return False
    
    soma = 0
    multiplicador = 11
    for i in range(10):
        soma += int(cpf[i]) * multiplicador
        multiplicador -= 1
    resto = soma % 11
    digito_verificador2 = 0 if resto < 2 else 11 - resto
    
    if int(cpf[10]) != digito_verificador2:
        return False
    
    return True

cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")

if valida_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")
