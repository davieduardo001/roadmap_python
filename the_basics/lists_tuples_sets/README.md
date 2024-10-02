# Estruturas de Dados em Python: Listas, Tuplas e Conjuntos

## 1. Listas

As listas em Python são coleções ordenadas e mutáveis de elementos. Elas podem conter elementos de diferentes tipos, incluindo outros objetos e até mesmo outras listas.

### Criando uma lista

```python
minha_lista = [1, 2, 3, 4, 5]
```

### Acessando elementos

Os elementos de uma lista podem ser acessados através de seus índices, começando em 0.

```python
print(minha_lista[0])  # Saída: 1
print(minha_lista[2])  # Saída: 3
```

### Modificando elementos

Os elementos em uma lista podem ser alterados.

```python
minha_lista[1] = 10
print(minha_lista)  # Saída: [1, 10, 3, 4, 5]
```

### Métodos comuns

- `append()`: Adiciona um elemento ao final da lista.
- `remove()`: Remove o primeiro elemento com o valor especificado.
- `pop()`: Remove e retorna o elemento no índice especificado.
- `sort()`: Ordena a lista.

## 2. Tuplas

As tuplas são semelhantes às listas, mas são imutáveis. Uma vez criadas, não podem ser alteradas.

### Criando uma tupla

```python
minha_tupla = (1, 2, 3, 4, 5)
```

### Acessando elementos

Assim como nas listas, os elementos das tuplas podem ser acessados através de seus índices.

```python
print(minha_tupla[0])  # Saída: 1
```

### Métodos comuns

As tuplas possuem menos métodos que as listas, mas alguns úteis incluem:

- `count()`: Retorna o número de ocorrências de um valor na tupla.
- `index()`: Retorna o índice do primeiro elemento com o valor especificado.

## 3. Conjuntos

Os conjuntos são coleções não ordenadas de elementos únicos. Eles são mutáveis, mas não permitem duplicatas.

### Criando um conjunto

```python
meu_conjunto = {1, 2, 3, 4, 5}
```

### Acessando elementos

Os conjuntos não suportam indexação, pois são não ordenados. Você pode verificar a presença de um elemento usando o operador `in`.

```python
print(3 in meu_conjunto)  # Saída: True
```

### Métodos comuns

- `add()`: Adiciona um elemento ao conjunto.
- `remove()`: Remove um elemento do conjunto. Levanta um erro se o elemento não estiver presente.
- `discard()`: Remove um elemento do conjunto, mas não levanta erro se o elemento não estiver presente.
- `union()`: Retorna a união de dois conjuntos.

## Exercícios

1. **Listas**: Crie uma lista contendo os números de 1 a 10 e, em seguida, adicione o número 11 a ela. Exiba a lista resultante.

2. **Tuplas**: Crie uma tupla com os nomes de cinco frutas. Em seguida, exiba a fruta na terceira posição da tupla.

3. **Conjuntos**: Crie um conjunto com os números 1, 2, 3, 4 e 5. Adicione o número 6 e remova o número 2. Exiba o conjunto resultante.

4. **Listas e Tuplas**: Crie uma lista com cinco números inteiros. Converta essa lista em uma tupla e exiba a tupla resultante.

---

Esse documento deve fornecer uma boa visão geral sobre listas, tuplas e conjuntos em Python, além de exercícios práticos para reforçar o aprendizado. Se precisar de mais detalhes ou explicações, estou à disposição!