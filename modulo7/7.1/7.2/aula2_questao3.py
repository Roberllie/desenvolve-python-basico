def verifica_palindromo(texto):

    texto_limpo = ''.join([char.lower() for char in texto if char.isalnum()])
    return texto_limpo == texto_limpo[::-1]

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == 'fim':
        break
    if verifica_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
