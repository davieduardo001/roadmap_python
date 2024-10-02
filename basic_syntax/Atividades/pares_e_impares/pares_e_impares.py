# 3. **Escreva um laço** que percorra uma lista de números e imprima apenas os números pares.

arr = [0]

for i in range(100):
    arr.append(i+1)

[print(i, ' é par') if arr[i] % 2 == 0 else print(i, ' é impar') for i in range(len(arr))]