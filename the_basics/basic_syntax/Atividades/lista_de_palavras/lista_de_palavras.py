# 5. **Escreva uma função** que receba uma lista de palavras e retorne a palavra mais longa.

palavras = []

op = 1

def verificar_palavra(arr_palavras):
    maior_palavra = arr_palavras[0]

    for palavra in arr_palavras:
        print(palavra)
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra

    return maior_palavra

while op != 0:
    print(f'Deseja adiciona mais uma palavra?')
    op = int(input(f'1. Sim\n0. Não\n'))
    
    if op == 1:
        palavra = input(f'Adicione mais uma palavra: ')
        palavras.append(palavra)
        print()
    else:
        print(f'maior palavra: {verificar_palavra(palavras)}') 