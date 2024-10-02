### Atividade 4: Identificação de Tipos
# Escreva um programa que receba um valor do usuário e identifique automaticamente o tipo de dado inserido (inteiro, ponto flutuante ou string).
# ```python
# valor = input("Digite algo: ")
# # Verifique o tipo de dado
# if valor.isdigit():
#    print("O valor é um número inteiro.")
# elif valor.replace('.', '', 1).isdigit():
#    print("O valor é um número decimal (float).")
# else:
#    print("O valor é uma string.")
#```

var = input('receber uma variavel: ')
if isinstance(var, str):
    print('É uma string')
elif isinstance(var, int):
    print('É um inteiro')
elif isinstance(var, float):
    print('É um float')