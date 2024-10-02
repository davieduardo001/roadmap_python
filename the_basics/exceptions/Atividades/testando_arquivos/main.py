#Escreva um programa que tenta abrir um arquivo chamado dados.txt para leitura. Se o arquivo não existir, ele deve exibir uma mensagem informando que o arquivo não foi encontrado. No final, o programa deve garantir que, se o arquivo for aberto, ele será fechado.
#Dicas: Use try, except FileNotFoundError e finally.

try:
    with open("arquivo.txt", "r") as arquivo:
        content = arquivo.read()
        print(content)
except FileNotFoundError:
    print('arquivo nn encontrado!')