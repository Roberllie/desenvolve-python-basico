import random
import math
n = int(input("Qtd de números: "))
soma = 0
for i in range(n):
    soma += random.randint(0,100)

print(f"A raiz quadrada dos {n} números informados é {math.sqrt(soma)}")
