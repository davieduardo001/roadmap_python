# Dada uma lista de números inteiros, crie um código para calcular a soma de todos os números pares da lista.

import random

lista_de_numeros = []
for _ in range(100):
    n = random.randint(1, 100)
    lista_de_numeros.append(n)

soma = sum(numero for numero in lista_de_numeros if (numero % 2 == 0))

print(f'{soma}')