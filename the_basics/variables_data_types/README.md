# Documentação: Variáveis e Tipos de Dados em Python

## Introdução
No Python, **variáveis** são usadas para armazenar dados que serão manipulados ao longo do programa. Python é uma linguagem de tipagem dinâmica, o que significa que você não precisa especificar o tipo de dado ao declarar uma variável; o Python identifica automaticamente o tipo com base no valor atribuído.

### O que é uma variável?

Uma **variável** é como uma "caixa" na memória onde guardamos valores, que podem ser modificados ao longo do programa. Em Python, basta atribuir um valor a um nome de variável.

### Definindo uma variável

Para declarar uma variável em Python, usamos o operador de atribuição `=`:

```python
nome = "Maria"      # String (texto)
idade = 25          # Inteiro (int)
altura = 1.70       # Ponto flutuante (float)
estudante = True    # Booleano (True ou False)
```

### Tipos de Dados em Python

Os tipos de dados mais comuns em Python são:

1. **Inteiros (`int`)**: Números inteiros, como 5, -20, 0.
   - Exemplo: `numero = 10`

2. **Ponto Flutuante (`float`)**: Números com casas decimais, como 3.14, -0.01.
   - Exemplo: `altura = 1.75`

3. **Strings (`str`)**: Sequências de caracteres, ou seja, texto.
   - Exemplo: `nome = "Ana"`

4. **Booleanos (`bool`)**: Verdadeiro ou falso, representado como `True` ou `False`.
   - Exemplo: `ativo = True`

5. **Listas (`list`)**: Armazenam uma coleção de valores de qualquer tipo.
   - Exemplo: `frutas = ["maçã", "banana", "laranja"]`

### Operações com Variáveis

Você pode realizar várias operações com variáveis, dependendo do tipo de dado.

#### Operações com números:

```python
x = 10
y = 5

soma = x + y            # Soma: 15
subtracao = x - y       # Subtração: 5
multiplicacao = x * y   # Multiplicação: 50
divisao = x / y         # Divisão: 2.0
```

#### Operações com strings:

```python
nome = "Maria"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome   # Concatenação: "Maria Silva"
```

### Funções Úteis

#### Saber o tipo de uma variável

Você pode verificar o tipo de dado de uma variável usando a função `type()`:

```python
idade = 25
print(type(idade))  # <class 'int'>
```

#### Conversão de Tipos (Casting)

Às vezes, é necessário converter um tipo de dado para outro. Isso pode ser feito com funções de conversão.

```python
# Convertendo inteiro para string
idade = 25
idade_str = str(idade)  # "25"

# Convertendo string para inteiro
numero_str = "10"
numero = int(numero_str)  # 10

# Convertendo string para float
numero_float = float("3.14")  # 3.14
```

### Boas Práticas

- Escolha **nomes descritivos** para suas variáveis.
- Mantenha a consistência dos tipos de dados ao realizar operações.
- Use comentários para explicar o código quando necessário.

---

## Atividades

### Atividade 1: Declaração de Variáveis

Crie um programa que declare as seguintes variáveis:
- Uma variável `nome` para armazenar o nome de uma pessoa (do tipo `string`).
- Uma variável `idade` que armazena a idade dessa pessoa (do tipo `int`).
- Uma variável `altura` que armazena a altura em metros (do tipo `float`).
- Uma variável `estudante` que indica se a pessoa é estudante (do tipo `boolean`).

Exiba todos os valores usando `print()`.

#### Exemplo de saída esperada:
```
Nome: Ana
Idade: 22
Altura: 1.68
É estudante? True
```

### Atividade 2: Operações com Variáveis

Escreva um programa que some, subtraia, multiplique e divida dois números inteiros. Mostre o resultado de cada operação no console.

```python
numero1 = 8
numero2 = 4

# Realize as operações e mostre o resultado
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
```

### Atividade 3: Conversão de Tipos

Dado o valor inteiro `45`, converta-o para uma string e concatene com a frase `" anos de idade"`. Mostre o resultado no console.

```python
idade = 45
idade_str = str(idade)
frase = idade_str + " anos de idade"
print(frase)
```

### Atividade 4: Identificação de Tipos

Escreva um programa que receba um valor do usuário e identifique automaticamente o tipo de dado inserido (inteiro, ponto flutuante ou string).

```python
valor = input("Digite algo: ")

# Verifique o tipo de dado
if valor.isdigit():
    print("O valor é um número inteiro.")
elif valor.replace('.', '', 1).isdigit():
    print("O valor é um número decimal (float).")
else:
    print("O valor é uma string.")
```