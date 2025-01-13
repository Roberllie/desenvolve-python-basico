 #Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade 
 #possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. 
 #A saída deve estar formatada exatamente como indicado.

saque = int(input("Valor do saque desejado: "))
cont_100 = 0
cont_50 = 0
cont_20 = 0
cont_10 = 0 
cont_5 = 0 
cont_2 = 0
cont_1 = 0 

while (saque >= 100):
    saque // 100
    cont_100 = cont_100 + 1
    saque = saque - 100
print (f"100: {cont_100}")

while (saque >= 50):
    saque // 50
    cont_50 = cont_50 + 1
    saque = saque - 50
print (f"50: {cont_50}")

while (saque >= 20):
    saque // 20
    cont_20 = cont_20 + 1
    saque = saque - 20
print (f"20: {cont_20}")

while (saque >= 10):
    saque // 10
    cont_10 = cont_10 + 1
    saque = saque - 10
print (f"10: {cont_10}")

while (saque >= 5):
    saque // 5
    cont_5 = cont_5 + 1
    saque = saque - 5
print (f"5: {cont_5}")

while (saque >= 2):
    saque // 2
    cont_2 = cont_2 + 1
    saque = saque - 2
print (f"2: {cont_2}")

while (saque >= 1):
    saque // 1
    cont_50 = cont_100 + 1
    saque = saque - 1
print (f"1: {cont_1}")
