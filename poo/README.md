# Programação Orientada a Objetos com Python

## Índice
1. [Introdução à Programação Orientada a Objetos](#1-introdução-à-programação-orientada-a-objetos)
2. [Classes e Objetos](#2-classes-e-objetos)
   - [Definindo uma Classe](#21-definindo-uma-classe)
   - [Criando Objetos](#22-criando-objetos)
3. [Atributos e Métodos](#3-atributos-e-métodos)
   - [Atributos de Instância](#31-atributos-de-instância)
   - [Métodos](#32-métodos)
   - [Atributos de Classe](#33-atributos-de-classe)
4. [Encapsulamento](#4-encapsulamento)
5. [Herança](#5-herança)
6. [Polimorfismo](#6-polimorfismo)
7. [Abstração](#7-abstração)

---

## 1. Introdução à Programação Orientada a Objetos

A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o software em torno de **objetos** que possuem **atributos** (dados) e **métodos** (funções). Este paradigma permite representar o mundo real no código de forma mais intuitiva, através de conceitos como classes, herança, encapsulamento, e polimorfismo.

**Principais conceitos da POO**:
- **Classe**: Uma estrutura que define um tipo de objeto, incluindo seus atributos e métodos.
- **Objeto**: Uma instância de uma classe.
- **Atributo**: Dados que descrevem o estado de um objeto.
- **Método**: Funções que definem o comportamento de um objeto.

## 2. Classes e Objetos

### 2.1. Definindo uma Classe
Uma classe em Python é criada usando a palavra-chave `class`. Dentro da classe, são definidos os atributos e métodos que os objetos dessa classe terão.

Exemplo básico de uma classe:
```python
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(f"{self.nome} está latindo.")
```

### 2.2. Criando Objetos
Um **objeto** é uma instância de uma classe. Para criar um objeto, basta chamar a classe como se fosse uma função.

Exemplo:
```python
meu_cachorro = Cachorro("Rex", 5)
print(meu_cachorro.nome)  # Saída: Rex
meu_cachorro.latir()  # Saída: Rex está latindo.
```

## 3. Atributos e Métodos

### 3.1. Atributos de Instância
Os **atributos de instância** são variáveis associadas a uma instância específica de uma classe. Eles são definidos geralmente no método `__init__()` e são únicos para cada objeto.

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
```

### 3.2. Métodos
Métodos são funções definidas dentro de uma classe que manipulam os atributos ou realizam operações específicas.

Exemplo de método:
```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def dirigir(self):
        print(f"O carro {self.marca} {self.modelo} está em movimento.")
```

### 3.3. Atributos de Classe
**Atributos de classe** são variáveis que são compartilhadas entre todas as instâncias da classe. Eles são definidos diretamente na classe e são comuns a todos os objetos criados.

```python
class Animal:
    reino = "Animalia"  # Atributo de classe

    def __init__(self, nome):
        self.nome = nome
```

```python
leao = Animal("Leão")
gato = Animal("Gato")
print(leao.reino)  # Saída: Animalia
print(gato.reino)  # Saída: Animalia
```

## 4. Encapsulamento
O encapsulamento é o conceito de restringir o acesso direto aos atributos e métodos de uma classe para proteger os dados. Em Python, isso é feito usando **atributos privados** (prefixados com `__`).

```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        self.__saldo += valor

    def obter_saldo(self):
        return self.__saldo
```

No exemplo acima, o atributo `__saldo` não pode ser acessado diretamente fora da classe.

## 5. Herança
A **herança** permite que uma classe herde atributos e métodos de outra classe. A classe que herda é chamada de **subclasse**, e a classe da qual ela herda é chamada de **superclasse**.

Exemplo de herança:
```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(f"{self.nome} está fazendo um som.")

class Cachorro(Animal):  # Cachorro herda de Animal
    def fazer_som(self):
        print(f"{self.nome} está latindo.")
```

```python
rex = Cachorro("Rex")
rex.fazer_som()  # Saída: Rex está latindo.
```

## 6. Polimorfismo
O **polimorfismo** permite que diferentes classes implementem o mesmo método de maneiras diferentes. Ou seja, o mesmo nome de método pode se comportar de maneira distinta dependendo da classe.

```python
class Ave:
    def emitir_som(self):
        print("A ave está cantando.")

class Pato(Ave):
    def emitir_som(self):
        print("O pato está grasnando.")

class Papagaio(Ave):
    def emitir_som(self):
        print("O papagaio está falando.")
```

```python
animais = [Pato(), Papagaio()]
for animal in animais:
    animal.emitir_som()
```
Saída:
```
O pato está grasnando.
O papagaio está falando.
```

## 7. Abstração
A **abstração** oculta os detalhes de implementação e mostra apenas as funcionalidades essenciais de um objeto. Em Python, isso pode ser implementado com **classes abstratas**, que são classes que não podem ser instanciadas diretamente.

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura
```

Neste exemplo, `Forma` é uma classe abstrata que define o método `area()`, que deve ser implementado por qualquer classe que herde dela.