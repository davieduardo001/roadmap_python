# Dada uma lista de números, encontre o maior e o menor valor da lista sem usar as funções max() ou min().

import random

arr = []

for _ in range(100):
    arr.append(random.randint(1, 100))

print(f'max: {max(arr)}')
print(f'min: {min(arr)}')