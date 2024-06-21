numero = input("Digite o número: ")

numero = numero.replace(" ", "").replace(".", "").replace("-", "")

if len(numero) == 8:
    numero_completo = f"9{numero[:4]}-{numero[4:]}"
elif len(numero) == 9:
    if numero[0] == '9':
        numero_completo = f"{numero[:5]}-{numero[5:]}"
    else:
        print("Número inválido.")
        exit()
else:
    print("Número inválido.")
    exit()

print(f"Número completo: {numero_completo}")
