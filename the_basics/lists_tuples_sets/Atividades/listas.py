# 1. **Listas**: Crie uma lista contendo os números de 1 a 10 e, em seguida, adicione o número 11 a ela. Exiba a lista resultante.

lista = []

for i in range(1, 11):
    lista.append(i)

lista.append(11)
print(lista)