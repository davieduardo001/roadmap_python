# Documentação de Programação Orientada a Objetos em Python

## 1. Introdução

A Programação Orientada a Objetos (POO) é um paradigma de programação que utiliza "objetos" para representar dados e métodos. Em Python, a POO é implementada por meio de classes, que servem como modelos para a criação de objetos.

## 2. Conceitos Básicos

### 2.1 Classe
Uma classe é uma estrutura que define um novo tipo de objeto. Ela pode conter atributos (variáveis) e métodos (funções) que descrevem o comportamento e as características dos objetos criados a partir dessa classe.

#### Exemplo:
```python
class Carro:
    # Construtor da classe
    def __init__(self, marca, modelo, ano):
        self.marca = marca  # Atributo
        self.modelo = modelo  # Atributo
        self.ano = ano  # Atributo

    # Método
    def descricao(self):
        return f"{self.ano} {self.marca} {self.modelo}"
```

### 2.2 Objeto
Um objeto é uma instância de uma classe. Quando você cria um objeto, você está criando uma nova instância daquela classe, com suas próprias características.

#### Exemplo:
```python
# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2021)
print(meu_carro.descricao())  # Saída: 2021 Toyota Corolla
```

### 2.3 Atributos
Os atributos são variáveis que pertencem a uma classe e definem as propriedades do objeto.

#### Exemplo:
```python
# Atributos do objeto meu_carro
print(meu_carro.marca)  # Saída: Toyota
print(meu_carro.ano)    # Saída: 2021
```

### 2.4 Métodos
Os métodos são funções definidas dentro de uma classe que descrevem os comportamentos dos objetos.

#### Exemplo:
```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print(f"{self.modelo} está ligado.")

# Usando o método ligar
meu_carro.ligar()  # Saída: Corolla está ligado.
```

## 3. Herança

A herança é um mecanismo que permite que uma classe herde atributos e métodos de outra classe. Isso promove a reutilização de código e a criação de uma hierarquia de classes.

### 3.1 Exemplo de Herança
```python
class Veiculo:  # Classe base
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo):  # Classe derivada
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo)  # Chamando o construtor da classe base
        self.ano = ano

    def descricao(self):
        return f"{self.ano} {self.marca} {self.modelo}"

# Criando um objeto da classe Carro
meu_carro = Carro("Honda", "Civic", 2022)
print(meu_carro.descricao())  # Saída: 2022 Honda Civic
```

## 4. Encapsulamento

O encapsulamento é o conceito de esconder os detalhes internos de um objeto e expor apenas o que é necessário. Em Python, os atributos podem ser privados ou públicos.

### 4.1 Atributos Privados
Atributos que não devem ser acessados diretamente fora da classe podem ser precedidos por um underscore (`_`).

#### Exemplo:
```python
class ContaBancaria:
    def __init__(self, saldo=0):
        self._saldo = saldo  # Atributo privado

    def deposito(self, valor):
        self._saldo += valor

    def saque(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Saldo insuficiente.")

    def get_saldo(self):
        return self._saldo

# Usando a classe ContaBancaria
conta = ContaBancaria()
conta.deposito(100)
print(conta.get_saldo())  # Saída: 100
```

## 5. Polimorfismo

O polimorfismo permite que diferentes classes implementem métodos com o mesmo nome, mas comportamentos diferentes.

### 5.1 Exemplo de Polimorfismo
```python
class Animal:
    def fazer_som(self):
        raise NotImplementedError("Subclasses devem implementar este método.")

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Usando polimorfismo
animais = [Cachorro(), Gato()]
for animal in animais:
    print(animal.fazer_som())  # Saída: Au au! Miau!
```

## 6. Conclusão

A Programação Orientada a Objetos em Python oferece uma maneira poderosa de organizar e estruturar o código, facilitando a reutilização e a manutenção. Compreender os conceitos de classes, objetos, herança, encapsulamento e polimorfismo é fundamental para aproveitar ao máximo as capacidades do Python.

## 7. Referências

- [Documentação oficial do Python](https://docs.python.org/3/tutorial/classes.html)
- [Programação Orientada a Objetos](https://pt.wikipedia.org/wiki/Programação_orientada_a_objetos)