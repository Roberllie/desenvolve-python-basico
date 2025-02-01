n1 = float(input("N1: "))
n2 = float(input("N2: "))
n3 = float(input("N3: "))

m = (n1 + n2 + n3)/3

if (m >= 60):
    print("Aprovado")
elif (m >= 40):
    print("Recuperação")
else:
    print("Reprovado")
