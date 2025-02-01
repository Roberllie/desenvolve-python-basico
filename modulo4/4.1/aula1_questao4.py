n = int(input("Digite n: "))
maior = 0

while n > maior:
    x = int(input("Digite x: "))
    if (x > maior):
        maior = x
        n -= 1 
    else: 
        n -= 1 

print (maior)
