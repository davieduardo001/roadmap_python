# Exercício 1: Divisão com Tratamento de Exceção
# Escreva um programa que solicita ao usuário dois números e tenta realizar a divisão. Se o usuário fornecer um valor que não seja numérico, ou tentar dividir por zero, o programa deve exibir uma mensagem de erro adequada.
# Dicas: Use try, except ValueError e except ZeroDivisionError.

n1 = int(input('Digite o primeiro numero'))
n2 = int(input('Digite o segundo numero'))

try:
    total = n1/n2
    print(f'{total}')
except ZeroDivisionError:
    print('nn eh possivel dividir por zero!')