### Atividade 1: Declaração de Variáveis
# Crie um programa que declare as seguintes variáveis:
# - Uma variável `nome` para armazenar o nome de uma pessoa (do tipo `string`).
# - Uma variável `idade` que armazena a idade dessa pessoa (do tipo `int`).
# - Uma variável `altura` que armazena a altura em metros (do tipo `float`).
# - Uma variável `estudante` que indica se a pessoa é estudante (do tipo `boolean`).
# Exiba todos os valores usando `print()`.
#### Exemplo de saída esperada:
# ```
# Nome: Ana
# Idade: 22
# Altura: 1.68
# É estudante? True
# ```

def receber_vars():
    nome = input('digite o nome: ')
    idade = int(input('digite a idade: '))
    altura = float(input('digite a altura: '))
    estudante = input('Digite Sim ou Não para ver se é estudante: ')
    if (estudante.lower() == 'sim'):
        estudante = True
    else:
        estudante = False

    print(f'nome: {nome}\nIdade: {idade}\nAltura: {altura}\nEstudante: {estudante}')

receber_vars()