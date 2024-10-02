
# 2. **Crie um programa** que peça ao usuário para digitar sua idade e informe se ele é maior ou menor de idade.

def maior_idade(idade):
    if idade >= 18:
        return True
    else:
        return False

idade = int(input('Escreva sua idade: '))

output = 'maior de idade' if maior_idade(idade) else 'menor idade'
printf(output)