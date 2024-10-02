
# 6. **Implemente um sistema simples de cadastro** que permita ao usuário adicionar, visualizar e remover nomes de uma lista.


def check_nome_exists(arr_nomes, nome):
    if nome in arr_nomes:
        return True
    else:
        return False

def add_nome(arr_nomes):
    nome = input('escreva um nome: ')

    arr_nomes.append(nome)

def remove_nome(arr_nomes):
    nome_to_remove = input('escreva o nome q deseja remover: ')

    if check_nome_exists(arr_nomes, nome_to_remove):
        arr_nomes.remove(nome_to_remove)
    else:
        print('nome nao existente na base de dados')

def print_nomes(arr_nomes):
    for nome in arr_nomes:
        print(f'{nome}')

def main():
    resp = 1
    nomes = []

    while resp != 0:
        resp = int(input(f'qual operacao deseja fazer?\n1. Adicionar nome\n2. Remover nome\n3. Listar nomes\n0. Sair do programa'))

        if resp == 0:
            print(f'saindo do programa')
            return 0
        elif resp == 1:
            add_nome(nomes)
        elif resp == 2:
            remove_nome(nomes)
        elif resp == 3:
            print_nomes(nomes)
        else:
            print(f'opcao nao existe')

main()