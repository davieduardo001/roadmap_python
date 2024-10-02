# Documentação sobre os Conceitos Básicos de Python

## Introdução

Python é uma linguagem de programação de alto nível, interpretada e orientada a objetos, com uma sintaxe simples e fácil de aprender. Ela é amplamente utilizada em diversas áreas, como desenvolvimento web, automação, ciência de dados, inteligência artificial, entre outras.

Neste documento, vamos explorar alguns dos conceitos básicos da linguagem, incluindo a sintaxe, tipos de dados, operadores, estruturas de controle de fluxo e funções. Ao final, há algumas atividades para você praticar seus conhecimentos.

---

## 1. Primeira Aplicação em Python

Existem duas maneiras principais de executar programas Python:
1. **Modo Interativo**: Executando diretamente no interpretador.
2. **Modo Script**: Escrevendo o código em um arquivo `.py` e executando o arquivo.

### Exemplo em Modo Interativo

No terminal, digite:

```bash
$ python3
```

Aparecerá o prompt `>>>`, onde você pode digitar comandos diretamente. Para imprimir uma mensagem, por exemplo:

```python
>>> print("Hello, World!")
```

### Exemplo em Modo Script

Crie um arquivo chamado `hello.py` com o seguinte conteúdo:

```python
print("Hello, World!")
```

Para executar o arquivo:

```bash
$ python3 hello.py
```

---

## 2. Identificadores

Identificadores são os nomes usados para variáveis, funções, classes, entre outros. Em Python, eles devem seguir estas regras:
- Devem começar com uma letra (A-Z, a-z) ou um sublinhado (_), seguidos por letras, números ou sublinhados.
- Python é **case-sensitive**, ou seja, `nome` e `Nome` são identificadores diferentes.
- Identificadores que começam com sublinhado único (_) são indicados para uso interno. Dois sublinhados no início e no final (__nome__) são reservados para métodos especiais da linguagem.

### Exemplo de Identificadores Válidos:

```python
variavel = 10
_nome = "Privado"
__metodo_interno__ = True
```

---

## 3. Palavras Reservadas

As palavras reservadas são termos que já têm um significado especial em Python e não podem ser usados como nomes de variáveis ou funções. Aqui estão alguns exemplos:

- `and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `False`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `None`, `not`, `or`, `pass`, `return`, `True`, `try`, `while`, `with`, `yield`

---

## 4. Indentação

Ao contrário de outras linguagens que utilizam chaves `{}` para definir blocos de código, Python usa **indentação**. Todas as linhas dentro de um mesmo bloco devem ter a mesma quantidade de espaços.

```python
if True:
    print("Este bloco está indentado")
else:
    print("Outro bloco")
```

Se a indentação for inconsistente, ocorrerá um erro de sintaxe.

---

## 5. Tipos de Dados em Python

Python suporta diversos tipos de dados. Aqui estão alguns dos principais:

- **Inteiros (int)**: Números inteiros, positivos ou negativos, sem parte fracionária.
- **Float**: Números reais com ponto flutuante.
- **String**: Sequências de caracteres delimitadas por aspas simples ou duplas.
- **Booleanos (bool)**: Representam valores lógicos `True` ou `False`.
- **Listas (list)**: Coleções mutáveis de itens ordenados.
- **Tuplas (tuple)**: Coleções imutáveis de itens ordenados.
- **Dicionários (dict)**: Estruturas de dados que armazenam pares de chave-valor.

### Exemplos:

```python
inteiro = 5
flutuante = 3.14
texto = "Olá, Mundo!"
booleano = True
lista = [1, 2, 3]
tupla = (4, 5, 6)
dicionario = {"nome": "João", "idade": 30}
```

---

## 6. Operadores

### Operadores Aritméticos

- `+` (soma)
- `-` (subtração)
- `*` (multiplicação)
- `/` (divisão)
- `//` (divisão inteira)
- `%` (módulo)
- `**` (exponenciação)

### Exemplo:

```python
a = 10
b = 3

print(a + b)  # Soma: 13
print(a - b)  # Subtração: 7
print(a * b)  # Multiplicação: 30
print(a / b)  # Divisão: 3.33
print(a // b) # Divisão inteira: 3
print(a % b)  # Resto: 1
print(a ** b) # Exponenciação: 1000
```

### Operadores Relacionais

- `==` (igual)
- `!=` (diferente)
- `>` (maior que)
- `<` (menor que)
- `>=` (maior ou igual)
- `<=` (menor ou igual)

### Operadores Lógicos

- `and` (e)
- `or` (ou)
- `not` (não)

---

## 7. Estruturas de Controle

### Condicionais

A estrutura `if` permite executar diferentes blocos de código com base em condições:

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

### Laços de Repetição

#### Laço `while`

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

#### Laço `for`

```python
nomes = ["Ana", "Bruno", "Carlos"]

for nome in nomes:
    print(nome)
```

---

## 8. Funções

Em Python, funções são definidas usando a palavra-chave `def`. Elas permitem organizar e reutilizar código.

### Exemplo:

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")  # Output: Olá, João!
```

---

## Atividades para Praticar

1. **Implemente uma função** que receba dois números e retorne a soma deles.
2. **Crie um programa** que peça ao usuário para digitar sua idade e informe se ele é maior ou menor de idade.
3. **Escreva um laço** que percorra uma lista de números e imprima apenas os números pares.
4. **Crie um programa** que peça ao usuário para digitar um número e retorne o fatorial desse número usando um laço `while`.
5. **Escreva uma função** que receba uma lista de palavras e retorne a palavra mais longa.
6. **Implemente um sistema simples de cadastro** que permita ao usuário adicionar, visualizar e remover nomes de uma lista.