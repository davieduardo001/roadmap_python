# Dada uma lista, crie um código que remove todos os valores duplicados e retorne uma lista apenas com valores únicos.

import random

arr = []

for _ in range(100):
    arr.append(random.randint(1, 100))

lista_sem_repeticoes = list(set(arr))

print(arr)
print(lista_sem_repeticoes)
