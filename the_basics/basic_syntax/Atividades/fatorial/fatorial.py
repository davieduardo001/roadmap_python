# 4. **Crie um programa** que peça ao usuário para digitar um número e retorne o fatorial desse número usando um laço `while`.

def pegar_numero():
    n = int(input('digite um numero: '))
    return n

def calcular_fatorial(n):
    total = n
    i = n

    while (i > 1):
        total *= (i-1)
        i -= 1

    return total

n = pegar_numero()
fat = calcular_fatorial(n)
print(f'fatorial de {n} é {fat}')