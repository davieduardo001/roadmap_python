## Documentação sobre Listas em Python

### O que é uma Lista?
Em Python, uma lista é uma coleção **ordenada** e **mutável** de elementos, que pode conter itens de qualquer tipo de dado (inteiros, strings, objetos, etc.). As listas são definidas usando colchetes `[]`, e os itens são separados por vírgulas.

### Criando uma Lista
Você pode criar uma lista simplesmente colocando os elementos dentro de colchetes.

```python
# Criando uma lista de números
numeros = [1, 2, 3, 4, 5]

# Criando uma lista de strings
frutas = ["maçã", "banana", "laranja"]
```

### Acessando Elementos da Lista
Os itens de uma lista são acessados usando **índices**. Os índices começam do zero.

```python
# Acessando o primeiro item da lista
primeira_fruta = frutas[0]  # "maçã"

# Acessando o último item da lista
ultima_fruta = frutas[-1]  # "laranja"
```

### Modificando Itens da Lista
As listas são mutáveis, ou seja, você pode modificar seus itens.

```python
# Modificando o segundo item da lista
frutas[1] = "manga"
print(frutas)  # ["maçã", "manga", "laranja"]
```

### Métodos Comuns de Listas
#### 1. **`append()`**: Adiciona um item ao final da lista.
```python
frutas.append("abacaxi")
```

#### 2. **`insert()`**: Insere um item em uma posição específica.
```python
frutas.insert(1, "uva")
```

#### 3. **`remove()`**: Remove a primeira ocorrência de um item específico.
```python
frutas.remove("manga")
```

#### 4. **`pop()`**: Remove e retorna o item de uma posição específica (ou o último item se a posição não for especificada).
```python
frutas.pop()  # Remove e retorna "abacaxi"
frutas.pop(0)  # Remove e retorna "maçã"
```

#### 5. **`sort()`**: Ordena a lista em ordem crescente.
```python
numeros.sort()
```

#### 6. **`reverse()`**: Inverte a ordem dos itens na lista.
```python
numeros.reverse()
```

#### 7. **`len()`**: Retorna o número de itens na lista.
```python
tamanho = len(frutas)
```

#### 8. **`count()`**: Conta o número de ocorrências de um item na lista.
```python
frutas.count("banana")
```

#### 9. **`clear()`**: Remove todos os itens da lista.
```python
frutas.clear()
```

### Iterando sobre uma Lista
Você pode usar um loop `for` para iterar sobre os itens de uma lista.

```python
for fruta in frutas:
    print(fruta)
```

### Compreensão de Listas
Python suporta uma sintaxe poderosa chamada **compreensão de listas**, que permite criar listas de maneira concisa.

```python
quadrados = [x ** 2 for x in range(5)]
print(quadrados)  # [0, 1, 4, 9, 16]
```

---

## Exercícios para Prática

### Exercício 1: Soma de Elementos da Lista
Crie uma lista de números inteiros e calcule a soma de todos os elementos da lista.

**Dicas**: Use a função `sum()` ou um loop `for`.

```python
numeros = [1, 2, 3, 4, 5]
# Seu código aqui
```

### Exercício 2: Encontrar o Maior e Menor Número
Dada uma lista de números, encontre o maior e o menor número da lista.

**Dicas**: Use as funções `max()` e `min()`.

```python
numeros = [10, 5, 7, 2, 9]
# Seu código aqui
```

### Exercício 3: Contar Ocorrências de um Elemento
Crie uma lista de frutas e conte quantas vezes uma fruta específica aparece na lista.

**Dicas**: Use o método `count()`.

```python
frutas = ["maçã", "banana", "laranja", "banana", "maçã"]
# Seu código aqui
```

### Exercício 4: Remover Duplicatas da Lista
Dada uma lista com valores duplicados, crie uma nova lista contendo apenas os valores únicos.

**Dicas**: Use um conjunto (`set()`) para eliminar duplicatas.

```python
numeros = [1, 2, 2, 3, 4, 4, 5]
# Seu código aqui
```

### Exercício 5: Inverter a Ordem dos Itens
Dada uma lista, inverta a ordem dos itens sem usar o método `reverse()`.

**Dicas**: Use slicing ou um loop.

```python
numeros = [1, 2, 3, 4, 5]
# Seu código aqui
```

---

Esses exercícios ajudam a praticar a manipulação básica de listas em Python, cobrindo operações essenciais como acesso, modificação, iteração e métodos comuns.