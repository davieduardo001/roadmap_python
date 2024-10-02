# Dicionários em Python

## 1. O que são Dicionários?

Os dicionários em Python são estruturas de dados que armazenam pares de chave-valor. Eles são mutáveis e não ordenados, permitindo que você acesse os valores por meio de suas chaves. Isso os torna extremamente úteis para armazenar dados que precisam de um mapeamento, como informações de cadastro ou configurações.

## 2. Criando um Dicionário

### Sintaxe

Você pode criar um dicionário usando chaves `{}` ou a função `dict()`.

```python
# Usando chaves
meu_dicionario = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Usando a função dict()
meu_dicionario2 = dict(nome="Maria", idade=25, cidade="Rio de Janeiro")
```

## 3. Acessando Valores

Os valores em um dicionário podem ser acessados usando suas chaves.

```python
print(meu_dicionario["nome"])  # Saída: João
print(meu_dicionario["idade"])  # Saída: 30
```

## 4. Modificando Valores

Os valores em um dicionário podem ser alterados através de suas chaves.

```python
meu_dicionario["idade"] = 31
print(meu_dicionario)  # Saída: {'nome': 'João', 'idade': 31, 'cidade': 'São Paulo'}
```

## 5. Adicionando Novos Pares de Chave-Valor

Você pode adicionar novos pares de chave-valor a um dicionário simplesmente atribuindo um valor a uma nova chave.

```python
meu_dicionario["profissão"] = "Engenheiro"
print(meu_dicionario)  # Saída: {'nome': 'João', 'idade': 31, 'cidade': 'São Paulo', 'profissão': 'Engenheiro'}
```

## 6. Removendo Pares de Chave-Valor

Você pode remover um par de chave-valor usando a palavra-chave `del` ou o método `pop()`.

```python
# Usando del
del meu_dicionario["cidade"]

# Usando pop()
idade = meu_dicionario.pop("idade")

print(meu_dicionario)  # Saída: {'nome': 'João', 'profissão': 'Engenheiro'}
print(idade)  # Saída: 31
```

## 7. Métodos Comuns

Aqui estão alguns métodos úteis que você pode usar com dicionários:

- `keys()`: Retorna uma visão das chaves no dicionário.
- `values()`: Retorna uma visão dos valores no dicionário.
- `items()`: Retorna uma visão dos pares de chave-valor.
- `get()`: Retorna o valor associado a uma chave, retornando `None` se a chave não existir.

### Exemplo

```python
# Usando métodos
print(meu_dicionario.keys())   # Saída: dict_keys(['nome', 'profissão'])
print(meu_dicionario.values()) # Saída: dict_values(['João', 'Engenheiro'])
print(meu_dicionario.items())  # Saída: dict_items([('nome', 'João'), ('profissão', 'Engenheiro')])
```

## 8. Dicionários Aninhados

Dicionários podem conter outros dicionários como valores, permitindo a criação de estruturas de dados complexas.

```python
dicionario_aninhado = {
    "pessoa1": {
        "nome": "Ana",
        "idade": 28
    },
    "pessoa2": {
        "nome": "Carlos",
        "idade": 35
    }
}

print(dicionario_aninhado["pessoa1"]["nome"])  # Saída: Ana
```

## 9. Exercícios

1. **Criar um Dicionário**: Crie um dicionário contendo informações sobre você, como nome, idade e cidade. Exiba essas informações.

2. **Modificar um Valor**: No dicionário criado no exercício anterior, modifique o valor da idade e exiba o dicionário atualizado.

3. **Adicionar um Novo Par**: Adicione um novo par chave-valor ao dicionário, representando sua profissão, e exiba o dicionário.

4. **Remover um Par**: Remova a chave que representa sua cidade e exiba o dicionário resultante.

5. **Dicionário Aninhado**: Crie um dicionário aninhado que contenha informações sobre dois livros, incluindo título, autor e ano de publicação. Exiba o autor do primeiro livro.