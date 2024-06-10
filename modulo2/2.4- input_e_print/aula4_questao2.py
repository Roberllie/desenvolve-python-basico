# Solicita ao usuário a temperatura em Fahrenheit
fahrenheit = int(input("Informe a temperatura em graus Fahrenheit: "))

# Converte a temperatura para Celsius
celsius = int((fahrenheit - 32) * (5 / 9))

# Exibe o resultado formatado
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")
