import random

def encrypt(nomes):
    chave = random.randint(1, 10)  
    nomes_cript = []
    
    for nome in nomes:
        nome_cript = ""
        for char in nome:
           
            novo_char = chr(ord(char) + chave)
            nome_cript += novo_char
        nomes_cript.append(nome_cript)
    
    return nomes_cript, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

nomes_cript, chave_aleatoria = encrypt(nomes)

print("Nomes criptografados:", nomes_cript)
print("Chave de criptografia:", chave_aleatoria)
