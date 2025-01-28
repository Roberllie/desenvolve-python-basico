#Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da 
# divisão do número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % 
# que retorna o resto de uma divisão. 

num1 = int(input("Digite um número: "))
num2 = int(input("Outro: "))

soma = num1 + num2 
div_2 = soma % 2 
print ("par" if div_2 == 0 else "impar"  )

