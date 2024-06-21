import random

def embaralha_letras(frase):
    palavras = frase.split()
    novas_palavras = []
    
    for palavra in palavras:
        if len(palavra) > 3:
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            palavra_embaralhada = palavra[0] + ''.join(meio) + palavra[-1]
            novas_palavras.append(palavra_embaralhada)
        else:
            novas_palavras.append(palavra)
    
    return ' '.join(novas_palavras)

frase = "Python é uma linguagem de programação"
resultado = embaralha_letras(frase)
print(resultado)  
