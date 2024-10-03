# Documentação Python

## Índice
1. [Estruturas de Dados & Algoritmos](#1-estruturas-de-dados--algoritmos)
   - [Arrays e Listas Ligadas](#11-arrays-e-listas-ligadas)
   - [Tabelas Hash](#12-tabelas-hash)
   - [Heaps, Pilhas e Filas](#13-heaps-pilhas-e-filas)
   - [Árvore Binária de Busca](#14-árvore-binária-de-busca)
   - [Recursão](#15-recursão)
   - [Algoritmos de Ordenação](#16-algoritmos-de-ordenação)
2. [Construído x Personalizado](#2-construído-x-personalizado)
   - [Módulos](#21-módulos)
   - [Lambdas](#22-lambdas)
   - [Decorators](#23-decorators)
   - [Iteradores](#24-iteradores)
   - [Expressões Regulares](#25-expressões-regulares)

---

## 1. Estruturas de Dados & Algoritmos

### 1.1. Arrays e Listas Ligadas
Arrays e Listas Ligadas são estruturas de dados fundamentais para armazenar coleções de elementos.

- **Array**: Um array é uma estrutura de dados linear em que elementos são armazenados contiguamente na memória e podem ser acessados por um índice. Os arrays são de tamanho fixo e permitem o acesso rápido a qualquer elemento.
  
- **Lista Ligada**: Uma lista ligada é uma coleção de elementos chamados "nós", onde cada nó contém um valor e uma referência para o próximo nó na sequência. Ao contrário dos arrays, as listas ligadas permitem inserções e remoções eficientes em qualquer ponto da lista, mas o acesso aos elementos é mais lento.

### 1.2. Tabelas Hash
Uma tabela hash é uma estrutura de dados que mapeia chaves a valores usando uma função hash. A função hash converte a chave em um índice para acessar o valor diretamente. As tabelas hash são muito eficientes para inserção, exclusão e busca de dados, desde que a função hash distribua as chaves uniformemente.

### 1.3. Heaps, Pilhas e Filas
- **Heap**: Um heap é uma estrutura de dados baseada em árvore que satisfaz a propriedade de heap, onde o elemento de maior (ou menor) valor é sempre o primeiro. Heaps são usados principalmente para implementar filas de prioridade.

- **Pilha (Stack)**: Uma pilha é uma estrutura de dados linear que segue o princípio LIFO (Last In, First Out). Operações principais incluem `push` (inserir no topo) e `pop` (remover do topo).

- **Fila (Queue)**: Uma fila é uma estrutura de dados linear que segue o princípio FIFO (First In, First Out). Os elementos são adicionados no final da fila e removidos do início.

### 1.4. Árvore Binária de Busca
Uma árvore binária de busca (BST - Binary Search Tree) é uma árvore em que cada nó tem no máximo dois filhos e o valor do nó à esquerda é sempre menor do que o valor do nó pai, enquanto o valor do nó à direita é sempre maior. Isso permite buscas, inserções e exclusões eficientes.

### 1.5. Recursão
Recursão é uma técnica em que uma função se chama repetidamente até que uma condição base seja satisfeita. É frequentemente usada para resolver problemas que podem ser divididos em subproblemas menores de natureza semelhante.

Exemplo de recursão:
```python
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
```

### 1.6. Algoritmos de Ordenação
Algoritmos de ordenação são métodos para reorganizar os elementos de uma lista ou array em uma determinada ordem, como ordem crescente ou decrescente. Alguns dos algoritmos de ordenação mais comuns são:
- **Bubble Sort**
- **Merge Sort**
- **Quick Sort**
- **Insertion Sort**

---

## 2. Construído x Personalizado

### 2.1. Módulos
Em Python, módulos são arquivos que contêm definições e instruções Python. Eles ajudam a organizar e reutilizar o código. Você pode importar módulos integrados ou criar seus próprios módulos personalizados.

Exemplo de importação de um módulo:
```python
import math
print(math.sqrt(16))  # Saída: 4.0
```

### 2.2. Lambdas
Lambdas são funções anônimas que podem ter qualquer número de argumentos, mas apenas uma expressão. Elas são úteis para funções curtas que você não precisa definir com um nome.

Exemplo de uma função lambda:
```python
dobro = lambda x: x * 2
print(dobro(5))  # Saída: 10
```

### 2.3. Decorators
Decorators são funções que modificam o comportamento de outras funções ou métodos. Eles permitem adicionar funcionalidades extras de forma concisa.

Exemplo de decorator:
```python
def meu_decorator(func):
    def wrapper():
        print("Algo antes da função")
        func()
        print("Algo depois da função")
    return wrapper

@meu_decorator
def minha_funcao():
    print("Executando a função")

minha_funcao()
```

### 2.4. Iteradores
Iteradores são objetos que podem ser iterados (percorridos), o que significa que você pode usar um loop para percorrer seus elementos. Em Python, iteradores implementam os métodos `__iter__()` e `__next__()`.

Exemplo de um iterador:
```python
meu_iter = iter([1, 2, 3])
print(next(meu_iter))  # Saída: 1
print(next(meu_iter))  # Saída: 2
```

### 2.5. Expressões Regulares
Expressões regulares (Regex) são padrões utilizados para buscar ou manipular cadeias de texto. Python oferece o módulo `re` para trabalhar com expressões regulares.

Exemplo básico de uso de regex:
```python
import re
padrao = r"\d+"  # Encontra sequências de dígitos
resultado = re.findall(padrao, "Temos 2 maçãs e 5 laranjas")
print(resultado)  # Saída: ['2', '5']
```