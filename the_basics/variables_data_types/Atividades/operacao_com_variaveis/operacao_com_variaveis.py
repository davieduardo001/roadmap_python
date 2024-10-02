
### Atividade 2: Operações com Variáveis
# Escreva um programa que some, subtraia, multiplique e divida dois números inteiros. Mostre o resultado de cada operação no console.
# ```python
# numero1 = 8
# numero2 = 4
# Realize as operações e mostre o resultado
# soma = numero1 + numero2
# subtracao = numero1 - numero2
# multiplicacao = numero1 * numero2
# divisao = numero1 / numero2
# print("Soma:", soma)
# print("Subtração:", subtracao)
# print("Multiplicação:", multiplicacao)
# print("Divisão:", divisao)
# ```

def receber_numeros():
    n1 = int(input('numero 1: '))
    n2 = int(input('numero 2: '))

    print(f'{n1} + {n2} = {n1+n2}')
    print(f'{n1} - {n2} = {n1-n2}')
    print(f'{n1} / {n2} = {n1/n2}')
    print(f'{n1} * {n2} = {n1*n2}')
    print(f'{n1} // {n2} = {n1//n2}')
    print(f'{n1} % {n2} = {n1%n2}')
    
receber_numeros()  